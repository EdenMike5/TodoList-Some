from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from sqlalchemy.orm import Session
from database import SessionLocal, Todo, engine, Base
import datetime

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins for development
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class TodoCreate(BaseModel):
    title: str

class TodoUpdate(BaseModel):
    completed: bool

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/todos")
def get_todos(db: Session = Depends(get_db)):
    todos = db.query(Todo).all()
    return [{"id": todo.id, "title": todo.title, "completed": todo.completed, "created_at": todo.created_at} for todo in todos]

@app.post("/todos")
def create_todo(todo: TodoCreate, db: Session = Depends(get_db)):
    db_todo = Todo(title=todo.title)
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return {"id": db_todo.id, "title": db_todo.title, "completed": db_todo.completed, "created_at": db_todo.created_at}

@app.put("/todos/{todo_id}")
def update_todo(todo_id: int, todo: TodoUpdate, db: Session = Depends(get_db)):
    db_todo = db.query(Todo).filter(Todo.id == todo_id).first()
    if not db_todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    db_todo.completed = todo.completed
    db.commit()
    db.refresh(db_todo)
    return {"id": db_todo.id, "title": db_todo.title, "completed": db_todo.completed, "created_at": db_todo.created_at}

@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int, db: Session = Depends(get_db)):
    db_todo = db.query(Todo).filter(Todo.id == todo_id).first()
    if not db_todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    db.delete(db_todo)
    db.commit()
    return {"message": "Todo deleted"}