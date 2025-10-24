from fastapi import APIRouter, Body, Depends, Path, Request
from fastapi.templating import Jinja2Templates

from sqlalchemy import delete, select, insert, update

from src.models import Todo
from src.config import settings
from src.dependencies import DB
from src.schemas import TodoAddRequest, TodoWitoutId, TodoSchema
from src.examples import TODO_UPDATE_EXAMPLES
from src.exceptions import (
    NotFoundHTTPError,
    TodoNotFoundHTTPError,
    TodoAlreadyExistsHTTPError,
)

templates = Jinja2Templates(directory=settings.BASE_DIR / "templates/")


router = APIRouter()


@router.post("/", status_code=201)
async def add_todo(
    db: DB,
    request: Request,
    todo: TodoAddRequest = Depends(TodoAddRequest.as_form),
) -> dict:
    query = select(Todo).filter(Todo.item == todo.item)
    result = await db.execute(query)
    existing_todo = result.scalar_one_or_none()
    if existing_todo:
        raise TodoAlreadyExistsHTTPError

    insert_stmt = insert(Todo).values(item=todo.item, status=todo.status)
    await db.execute(insert_stmt)
    await db.commit()

    query = select(Todo)
    result = await db.execute(query)
    todo_list = result.scalars().all()
    todo_list = [TodoSchema.model_validate(todo) for todo in todo_list]

    return templates.TemplateResponse(
        "todo.html",
        {
            "request": request,
            "todos": todo_list,
        },
    )


@router.get("/")
async def retrieve_todos(db: DB, request: Request) -> dict:
    query = select(Todo)
    result = await db.execute(query)
    todos = result.scalars().all()

    todos_list = [TodoSchema.model_validate(todo) for todo in todos]
    return templates.TemplateResponse(
        "todo.html",
        {
            "request": request,
            "todos": todos_list,
        },
    )


@router.get("/{todo_id}")
async def get_single_todo(
    db: DB,
    request: Request,
    todo_id: int = Path(title="The ID of the todo to retrieve.", min=1),
) -> dict:
    query = select(Todo).filter_by(id=todo_id)
    result = await db.execute(query)
    todo = result.scalar_one_or_none()
    if not todo:
        raise TodoNotFoundHTTPError

    return templates.TemplateResponse(
        "todo.html",
        {
            "request": request,
            "todo": todo,
        },
    )


@router.put("/{todo_id}")
async def update_todo(
    db: DB,
    todo_data: TodoWitoutId = Body(openapi_examples=TODO_UPDATE_EXAMPLES),
    todo_id: int = Path(..., title="The ID of the todo to be updated"),
) -> dict:
    query = select(Todo).filter_by(id=todo_id)
    result = await db.execute(query)
    todo = result.scalar_one_or_none()
    if not todo:
        raise TodoNotFoundHTTPError

    update_stmt = (
        update(Todo).where(Todo.id == todo_id).values(**todo_data.model_dump())
    )
    await db.execute(update_stmt)

    query = select(Todo).filter_by(id=todo_id)
    result = await db.execute(query)
    todo = result.scalar_one_or_none()

    await db.commit()

    return {
        "message": "Todo updated successfully.",
        "todo": TodoSchema.model_validate(todo).model_dump(),
    }


@router.delete("/{todo_id}")
async def delete_single_todo(db: DB, todo_id: int) -> dict:
    query = select(Todo).filter_by(id=todo_id)
    result = await db.execute(query)
    todo = result.scalar_one_or_none()
    if not todo:
        raise TodoNotFoundHTTPError

    delete_stmt = delete(Todo).where(Todo.id == todo_id)
    await db.execute(delete_stmt)
    await db.commit()
    return {"message": "Todo deleted successfully."}


@router.delete("/")
async def delete_all_todo(db: DB) -> dict:
    query = select(Todo)
    result = await db.execute(query)
    if not result.scalars().all():
        raise NotFoundHTTPError(detail="Todos list already empty")
    delete_stmt = delete(Todo)
    await db.execute(delete_stmt)
    await db.commit()
    return {"message": "Todos deleted successfully."}
