from fastapi import APIRouter,HTTPException
from database.book.db import Book
from database.member.db import Members
from models.member.modle import Create_member,Update_member
from logger import logger

router = APIRouter()

members = Members()
@router.post("",status_code=201)
def create_member(body:Create_member):
    data = members.create_member(body)
    logger.info(f"Created member ID: {data}")  
    return {"message":f"the member {data} created"}
@router.get("")
def get_all_members():

    data = members.get_the_members()
    logger.info("end get_all_members")

    return {"message":data}
@router.get("/{id}")
def get_member_by_id(id:int):

    data = members.get_by_id(id)
    if not data :
        logger.warning("error get_all_members")
        raise HTTPException(status_code=404,detail=f"id {id} not found")

    return {"message":data}

@router.patch("/{id}")
def update_member(id:int, data:Update_member):
    logger.info(f"start update_member id {id}")

    body = data.model_dump(exclude_none=True)
    if not body:
        logger.warning("error update_member no parameters")
        raise HTTPException (status_code=400,detail="no data to update")
    is_changde = members.patch_member(id,body)
    if not is_changde:
        logger.warning(f"error id {id}not found")
        raise HTTPException(status_code=404,detail=f"id {id} not found")
    logger.info(f"id {id} changde")
    return {"message":f"the member with id {id} changde"}
@router.patch("/{id}/deactivate")
def deactivate_member(id):

    data = members.disactivate_member(id)
    if not data :
        logger.warning(f"id {id}not found")
        raise HTTPException(status_code=404,detail=f"id {id}not found")
    logger.info("")
    return {"message":data}
@router.patch("/{id}/activate")
def to_activate_member(id):
    data = members.activate_member(id)
    if not data :
        logger.warning(f"id {id}not found")
        raise HTTPException(status_code=404,detail=f"id {id}not found")
    logger.info(f"Activated member ID: {id}")
    return {"message": f"Member {id} activated"}
