
class Todo(Base):
    __tablename__ = 'todos'
    
    id = Column(Integer, primary_key = True)
    title = Column(String, max_length=255)
    completed = Column(Boolean, default=False)