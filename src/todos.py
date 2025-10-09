from fastapi import APIRouter, Body, Path

from src.schemas import Todo
from src.examples import TODO_EXAMPLES

router = APIRouter()

todo_list = []


@router.post("/")
async def add_todo(
    todo: Todo = Body(
        description="The todo to add to the list.",
        openapi_examples=TODO_EXAMPLES,
    ),
) -> dict:
    for existing_todo in todo_list:
        if existing_todo.id == todo.id:
            return {"message": "Todo with supplied ID already exists."}
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


@router.get("/todo/{todo_id}")
async def get_single_todo(
    todo_id: int = Path(title="The ID of the todo to retrieve.", min=1),
) -> dict:
    for todo in todo_list:
        if todo.id == todo_id:
            return {"todo": todo}
    return {"message": "Todo with supplied ID doesn't exist."}
