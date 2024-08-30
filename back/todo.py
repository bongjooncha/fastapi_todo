from fastapi import APIRouter, Path, HTTPException, status
from model import Todo, TodoItem, TodoItems

todo_router = APIRouter()

todo_list = []

@todo_router.post("/todo")
async def add_todo(todo: TodoItem) -> dict:
    new_todo = Todo(id=len(todo_list) + 1, item=todo.item)
    todo_list.append(new_todo)
    return {"message": "Todo added successfully"}

@todo_router.get("/todo")
async def retrieve_todo() -> dict:
    return {
        "todos": todo_list
    } 



@todo_router.get("/todo/{todo_id}")
async def get_single_todo(todo_id: int) -> dict:
    for todo in todo_list:
        if todo.id == todo_id:
            return{"todo": todo}
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Todo with supplied ID doesn't exist"
    )

@todo_router.put("/todo/{todo_id}")
async def update_todo(todo_data: TodoItem, todo_id:int = Path(...,title="the Id of the todo to be updataed")) -> dict:
    for todo in todo_list:
        if todo.id == todo_id:
            todo.item = todo_data.item
            return{
                "message" : "Todo updated successfully"
            }
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Todo with supplied ID doesn't exist"
    )

@todo_router.delete("/todo/{todo_id}")
async def delete_single_todo(todo_id: int) -> dict:
    for index in range(len(todo_list)):
        todo = todo_list[index]
        if todo.id == todo_id:
            todo_list.pop(index)
            return {
                "message": "Todo deleted successfully"
            }
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Todo with supplied ID doesn't exist"
    )

