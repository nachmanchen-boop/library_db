from fastapi import APIRouter,HTTPException
from models.book.modle import Create_book,Patch_book,Ret_bro
from database.book.db import Book
router = APIRouter()
book = Book()
@router.post("",status_code=201)
def creatr_book(data:Create_book):
    last_Id = book.create_book(data)
    return {"message":last_Id}
@router.get("")
def get_all_books():
    data = book.get_the_books()
    return {"message":data}
@router.get("/{id}")
def get_book_by_id(id:int):
    data = book.get_by_id(id)
    if not data :
        raise HTTPException(status_code=404,detail=f"the id {id} not found")
    return {"message":data}
@router.patch("/{id}")
def update_book(id:int, body:Patch_book):
    data = body.model_dump(exclude_none=True)
    if not data:
        raise HTTPException (status_code=400,detail="nodata to update")
    is_changde = book.update_by_id(id=id,data=data)
    if not is_changde:
        raise HTTPException(status_code=404,detail=f"id {id} not found")
    return {"message":f"the bookk with id {id} changde"}
@router.patch("/{id}/borrow/{member_id}")
def set_not_available(body:Ret_bro):
    data = book.set_available(body)
    return data
    

    
@router.patch("/{id}/return/{member_id}")
def set_is_available(body:Ret_bro):
    data = book.set_available(body)
    return data