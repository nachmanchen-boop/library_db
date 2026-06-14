from pydantic import BaseModel,Field
from pydantic import BaseModel
from typing import Optional
from enum import Enum

class Enum_genre(str,Enum):
    Fiction="Fiction"
    Non_Fiction="Non-Fiction"
    Science="Science"
    Other="Other"
class Create_book(BaseModel):
    title:str =Field(min_length=0,max_length=50)
    author:str = Field(min_length=0 , max_length=50)
    genre : Enum_genre
    is_available : bool
    borrowed_by_member_id : int = None


class Patch_book(BaseModel):
    title:Optional[str] =Field(default=None,min_length=0,max_length=50)
    author:Optional[str] = Field(default=None,min_length=0 , max_length=50) 
    genre : Optional[Enum_genre] = None
    is_available :Optional[bool] =None
    borrowed_by_member_id : Optional[int] = None

class Ret_bro_enum(str,Enum):
    ret="return"
    borrow="borrow"
class Ret_bro(BaseModel):
    id :int
    ret_bro:Ret_bro_enum
    member_id:int