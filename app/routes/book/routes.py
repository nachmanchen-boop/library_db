from fastapi import APIRouter
from models.book.modle import create_book
from database.book.db import Book
router = APIRouter()
book = Book()
@router.post("",status_code=201)
def creatr_book(data:create_book):
    last_Id = book.create_book(data)
    return {"message":last_Id}