from fastapi import APIRouter,HTTPException
from models.book.modle import Create_book,Patch_book,Ret_bro
from database.book.db import Book
router = APIRouter()
book = Book()
from logger import logger

@router.post("",status_code=201)
def creatr_book(data:Create_book):
    last_Id = book.create_book(data)
    logger.info("end creatr_book")
    return {"message":last_Id}
@router.get("")
def get_all_books():
    data = book.get_the_books()
    logger.info("get_all_books")
    return {"message":data}
@router.get("/{id}")
def get_book_by_id(id:int):
    data = book.get_by_id(id)
    if not data :
        logger.warning(f"the id {id} not found")
        raise HTTPException(status_code=404,detail=f"the id {id} not found")
    logger.info("get_book_by_id")

    return {"message":data}
@router.patch("/{id}")
def update_book(id:int, body:Patch_book):
    data = body.model_dump(exclude_none=True)
    if not data:
        logger.warning("nodata to update")

        raise HTTPException (status_code=400,detail="nodata to update")
    is_changde = book.update_by_id(id=id,data=data)
    if not is_changde:
        logger.warning(f"id {id} not found")

        raise HTTPException(status_code=404,detail=f"id {id} not found")
    logger.info(f"the bookk with id {id} changde")
    return {"message":f"the bookk with id {id} changde"}
@router.patch("/{id}/borrow/{member_id}")
def set_not_available(body:Ret_bro):
    data = book.set_available(body)
    logger.info("end set_not_available")
    return data
    

    
@router.patch("/{id}/return/{member_id}")
def set_is_available(body:Ret_bro):
    data = book.set_available(body)
    
    logger.info("end set_is_available")


    return data