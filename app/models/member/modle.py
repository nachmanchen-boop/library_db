from pydantic import BaseModel,Field
from pydantic import BaseModel
from typing import Optional
from enum import Enum
class Create_member(BaseModel):
    name:str = Field(min_length=1,max_length=50)
    email:str = Field(min_length=5,max_length=50)
class Update_member(BaseModel):
    name:Optional[str] = Field(default=None,min_length=1,max_length=50)
    email:Optional[str] = Field(default=None,min_length=5,max_length=50)
    is_activ : bool|None = None
    total_borrows : int | None =None



  
