from pydantic import BaseModel,Field
from pydantic import BaseModel
from typing import Optional
from enum import Enum

class enum_genre(str,Enum):
    Fiction="Fiction"
    Non_Fiction="Non-Fiction"
    Science="Science"
    Other="Other"
class create_book(BaseModel):
    title:str =Field(min_length=0,max_length=50)
    author:str = Field(min_length=0 , max_length=50)
    genre : enum_genre
    is_available : bool
    borrowed_by_member_id : int = None




