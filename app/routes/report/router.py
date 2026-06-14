from fastapi import APIRouter,HTTPException
from database.book.db import Book
from database.member.db import Members
from models.member.modle import Create_member,Update_member
book = Book()
member =Members()
router = APIRouter()
@router.get("/summary")
def report():
    return {
        "total_books":book.get_count_books(),
        "available_books":book.get_count_available_books(),
        "currently_brroowed":book.get_count_not_available_books(),
        "active_members":member.get_count_activ_members()

    }
@router.get("/books-by-genre")
def count_by_genre(genre:str):
    data = book.books_by_genre(genre)
    return data
@router.get("/top-member")
def get_top_borrowing_member():
    data = book.top_count()
    
    if not data:
        raise HTTPException(status_code=404, detail="No members found in the system")
        
    return data