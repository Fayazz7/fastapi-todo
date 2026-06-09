from pydantic import BaseModel
from fastapi import APIRouter

router = APIRouter(
    prefix="/todos",
    tags=['todos']
)

todos = []

class ToDo(BaseModel):
    id: int
    title: str
    completed: bool = False

@router.get("/")
def home():
    return {"message": "Hello world!!"} 

@router.post("/create")
def create_todo(todo: ToDo):
    todos.append(todo)
    
    return {
        "message": "Todo Created",
        "todo": todo
    }
    
@router.get("/list")
def list_todos():
    return todos
