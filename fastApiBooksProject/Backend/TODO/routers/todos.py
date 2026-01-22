from typing import Annotated
from models import Todos
from fastapi import Depends, APIRouter, HTTPException, Path
from sqlalchemy.orm import Session
from starlette import status
from database import SessionLocal
import pydentic_model



router = APIRouter()


def get_db():
    
    db = SessionLocal()
    try:
        yield db
    finally : 
        db.close()
        
db_dependecny = Annotated[Session,Depends(get_db)]

@router.get("/",status_code=status.HTTP_200_OK)
async def get_todo_list(db:db_dependecny):
    return db.query(Todos).all()

@router.get("/todo/{todo_id}")
async def get_todo_by_id(db:db_dependecny,todo_id:int = Path(gt=0)):
    todo_model = db.query(Todos).filter(Todos.id == todo_id).first()
    if todo_model is not None:
        return todo_model
    raise HTTPException(status_code=404)

@router.post("/todo")
async def create_todo(db:db_dependecny,todo_request:pydentic_model.TodoRequest):
    todo_model = Todos(**todo_request.dict())
    db.add(todo_model)
    db.commit()
    
@router.put("/todo/{todo_id}")
async def update_todo(db:db_dependecny,todo_request:pydentic_model.TodoRequest,todo_id:int = Path(gt=0)):
    todo_model = db.query(Todos).filter(Todos.id == todo_id).first()
    if todo_model is None:
        raise HTTPException(status_code=404)
    todo_model.description = todo_request.description
    todo_model.title = todo_request.title
    todo_model.priority = todo_request.priority
    todo_model.complete = todo_request.complete
    db.add(todo_model)
    db.commit()
    
@router.delete("/todo/{todo_id}",status_code=status.HTTP_204_NO_CONTENT)
async def delete_todo(db:db_dependecny,todo_id:int = Path(gt=0)):
    todo_model = db.query(Todos).filter(todo_id==Todos.id).first()
    if todo_model is None:
        raise HTTPException(status_code=404)
    todo_model.delete()
    db.commit()