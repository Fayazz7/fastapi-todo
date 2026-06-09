from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

todos = []

class ToDo(BaseModel):
    id: int
    title: str
    completed: bool = False

@app.get("/")
def home():
    return {"message": "Hello world!!"} 

@app.post("/todo")
def create_todo(todo: ToDo):
    todos.append(todo)
    
    return {
        "message": "Todo Created",
        "todo": todo
    }
    
@app.get("/todos")
def list_todos():
    return todos


