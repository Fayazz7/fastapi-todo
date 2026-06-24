from pydantic import BaseModel
from fastapi import Depends
from fastapi import APIRouter
from sqlalchemy import select
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.todo import TodoCreate, TodoResponse
from app.models.todo import Todo

router = APIRouter(
    prefix="/todos",
    tags=['todos']
)

@router.get("/")
def home():
    return {"message": "Hello world!!"} 

@router.post("/create", response_model=TodoResponse)
def create_todo(todo:TodoCreate, db:Session=Depends(get_db)):
    todo = Todo(title=todo.title)
    db.add(todo)
    db.commit()
    db.refresh(todo)
    return todo
    
@router.get("/list", response_model=list[TodoResponse])
def list_todos(db:Session=Depends(get_db)):
    statement = select(Todo)
    results = db.execute(statement=statement)
    todos = results.scalars().first()
    return todos
