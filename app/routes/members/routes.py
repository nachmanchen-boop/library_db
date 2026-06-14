from fastapi import APIRouter,HTTPException
from database.book.db import Book
from database.member.db import Members
from models.member.modle import Create_member,Update_member

router = APIRouter()

members = Members()
@router.post("")
def create_member(body:Create_member):
    data = members.create_member(body)
    return {"message":f"the member {data} created"}
@router.get("")
def get_all_members():
    data = members.get_the_members()
        
    return {"message":data}
@router.get("/{id}")
def get_member_by_id(id:int):
    data = members.get_by_id(id)
    if not data :
        raise HTTPException(status_code=404,detail=f"id {id} not found")
    return {"message":data}

@router.patch("/{id}")
def update_member(id:int, data:Update_member):
    body = data.model_dump(exclude_none=True)
    if not body:
        raise HTTPException (status_code=400,detail="no data to update")
    is_changde = members.patch_member(id,body)
    if not is_changde:
        raise HTTPException(status_code=404,detail=f"id {id} not found")
    return {"message":f"the member with id {id} changde"}
@router.patch("/{id}/deactivate")
def deactivate_member(id):
    data = members.disactivate_member(id)
    if not data :
        raise HTTPException(status_code=404,detail=f"id {id}not found")
    return {"message":data}
@router.patch("/{id}/activate")
def deactivate_member(id):
    data = members.activate_member(id)
    if not data :
        raise HTTPException(status_code=404,detail=f"id {id}not found")
    return {"message":data}
