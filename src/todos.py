from fastapi import APIRouter, Body, Path

from src.schemas import Todo, TodoWitoutId
from src.examples import TODO_EXAMPLES, TODO_UPDATE_EXAMPLES
from src.exceptions import (
    NotFoundHTTPError,
    TodoNotFoundHTTPError,
    TodoAlreadyExistsHTTPError,
)

router = APIRouter()

todo_list = []


@router.post("/", status_code=201)
async def add_todo(
    todo: Todo = Body(
        description="The todo to add to the list.",
        openapi_examples=TODO_EXAMPLES,
    ),
) -> dict:
    for existing_todo in todo_list:
        if existing_todo.id == todo.id:
            raise TodoAlreadyExistsHTTPError
    todo_list.append(todo)
    return {
        "message": "Todo added successfully",
        "data": todo,
    }


@router.get("/")
async def retrieve_todos() -> dict:
    return {
        "todos": todo_list,
    }


@router.get("/{todo_id}")
async def get_single_todo(
    todo_id: int = Path(title="The ID of the todo to retrieve.", min=1),
) -> dict:
    for todo in todo_list:
        if todo.id == todo_id:
            return {"todo": todo}
    raise TodoNotFoundHTTPError


@router.put("/{todo_id}")
async def update_todo(
    todo_data: TodoWitoutId = Body(openapi_examples=TODO_UPDATE_EXAMPLES),
    todo_id: int = Path(..., title="The ID of the todo to be updated"),
) -> dict:
    for todo in todo_list:
        if todo.id == todo_id:
            todo.item = todo_data.item
            return {"message": "Todo updated successfully.", "data": todo}
    raise TodoNotFoundHTTPError


@router.delete("/{todo_id}")
async def delete_single_todo(todo_id: int) -> dict:
    for index in range(len(todo_list)):
        todo = todo_list[index]
        if todo.id == todo_id:
            todo_list.pop(index)
            return {"message": "Todo deleted successfully."}
    raise TodoNotFoundHTTPError


@router.delete("/")
async def delete_all_todo() -> dict:
    if not todo_list:
        raise NotFoundHTTPError(detail="Todos list already empty")
    todo_list.clear()
    return {"message": "Todos deleted successfully."}
