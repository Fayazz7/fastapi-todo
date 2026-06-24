from pydantic import BaseModel
from fastapi import Depends, APIRouter, Response
from fastapi.exceptions import HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.todo import TodoCreate, TodoResponse, TodoUpdate
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
    todos = results.scalars()
    return todos

@router.patch("/{todo_id}", response_model=TodoResponse)
def update_todo(todo_id: int, todo_in:TodoUpdate,  db:Session = Depends(get_db)):
    statement = select(Todo).where(Todo.id == todo_id)
    result = db.execute(statement)
    todo = result.scalar()
    if not todo:
        raise HTTPException(status_code=404, detail="Todo Not found")
    update_data = todo_in.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(todo, key, value)
    db.commit()
    db.refresh(todo)
    return todo

@router.delete("/{todo_id}")
def delete_todo(todo_id: int, db:Session = Depends(get_db)):
    statement = select(Todo).where(Todo.id == todo_id)
    result = db.execute(statement)
    todo_obj = result.scalar()
    if not todo_obj:    
        raise HTTPException(status_code=404, detail="Todo Not found")
    
    db.delete(todo_obj)
    db.commit()
    return Response(status_code=204)
    
