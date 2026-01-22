from typing import Annotated
from models import Users
from database import SessionLocal
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends
import pydentic_model
from starlette import status
from passlib.context import CryptContext

router = APIRouter()
bcrypt_context = CryptContext(schemes=['bcrypt'],deprecated='auto')

def get_db():
    
    db = SessionLocal()
    try:
        yield db
    finally : 
        db.close()
        
db_dependecny = Annotated[Session,Depends(get_db)]

@router.get("/users",status_code=status.HTTP_200_OK)
async def get_users(db:db_dependecny):
    return db.query(Users).all()

@router.post("/user")
async def create_user(db:db_dependecny,user_request: pydentic_model.UserRequest):
    user_model = Users(
        email = user_request.email,
        username = user_request.username,
        first_name = user_request.first_name,
        last_name = user_request.last_name,
        hashed_password = bcrypt_context.hash(user_request.password),
        is_active = user_request.is_active,
        role = user_request.role
    )
    db.add(user_model)
    db.commit()