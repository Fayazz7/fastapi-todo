from sqlalchemy import Column, String, Boolean, Integer
from app.database import Base

class Todo(Base):
    __tablename__ = 'todos'
    
    id = Column(Integer, primary_key = True)
    title = Column(String(255))
    completed = Column(Boolean, default=False)