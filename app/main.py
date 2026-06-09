from fastapi import FastAPI

from app.routers.todos import router

app = FastAPI()

app.include_router(router)