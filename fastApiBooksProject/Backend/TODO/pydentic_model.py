from pydantic import BaseModel, Field


class TodoRequest(BaseModel):
    title : str = Field(min_length=2,max_length=22)
    description : str = Field(min_length=5,max_length=52)
    priority : int = Field(gt=0,lt=6)
    complete : bool
    
class UserRequest(BaseModel):
    email : str = Field(min_length=10,max_length=52)
    username : str = Field(min_length=2,max_length=22)
    first_name : str = Field(min_length=2,max_length=22)
    last_name : str = Field(min_length=2,max_length=22)
    password : str = Field(min_length=2,max_length=52)
    is_active : bool
    role : str = Field(min_length=2,max_length=22)