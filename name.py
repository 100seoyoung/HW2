from fastapi import APIRouter, Path 
from model import Todo 

todo_router = APIRouter() 
todo_list = [] 
todo_counter = 0

@todo_router.post("/todo")
async def add_todo(todo: Todo) -> dict:
    global todo_counter
    todo.id = todo_counter + 1
    todo_list.append(todo)
    return { 
        "msg" : "todo added successfully" 
    
    }
    
@todo_router.get("/todo") 
async def retrieve_ todos() -> dict: 
    return { 
        "todos" : todo_list
    }
    
@todo_router.get("/todo/{todo_id}")
async def get_single_todo(todo.id: int = Path(..., title = "the ID of the todo to retrieve")) -> dict:
    for todo in todo_list:
        if todo. id == todo_id:
            return { "todo" : todo} 
    return {"msg" : "todo with supplied ID doesn 't exist"}