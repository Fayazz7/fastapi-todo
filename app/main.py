from fastapi import FastAPI
from app.database import Base, engine
from app.models.todo import Todo

from app.routers.todos import router as todos_router

app = FastAPI()

app.include_router(todos_router)

Base.metadata.create_all(bind=engine)