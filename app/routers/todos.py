from pydantic import BaseModel
from fastapi import APIRouter
from app.schemas.todo import TodoCreate, TodoResponse

router = APIRouter(
    prefix="/todos",
    tags=['todos']
)

todos = []

@router.get("/")
def home():
    return {"message": "Hello world!!"} 

@router.post("/create", response_model=TodoResponse)
def create_todo(todo: TodoCreate):
    todos.append(todo)
    
    return todo
    
@router.get("/list")
def list_todos():
    return todos
