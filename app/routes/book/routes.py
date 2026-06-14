from fastapi import APIRouter,HTTPException
from models.book.modle import create_book
from database.book.db import Book
router = APIRouter()
book = Book()
@router.post("",status_code=201)
def creatr_book(data:create_book):
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

