from typing import Optional
from pydantic import BaseModel,Field
class BookRequest(BaseModel):
    id : Optional[int] = Field(description="Id not required during book creation",default=None)
    name : str = Field(min_length=2, max_length=22)
    author : str = Field(min_length=2,max_length=22)
    rating : int = Field(gt=-1,lt=11)
    published_year : int = Field(lt=2026)
    
    model_config = {
        "json_schema_extra":{
            "example":{
                "name":"name of the book",
                "author":"author of the book",
                "rating":"rating of the book",
                "published_year":"year when the book is published"
            }
        }
    }