from database.db.db_connection import get_connection
from models.book.modle import Create_book,Ret_bro
from fastapi import HTTPException
from database.member.db import Members
members = Members()
class Book():
    def create_book(self,data:Create_book):
        with get_connection() as conn :
            with conn.cursor(dictionary=True) as cursor:
                query = """
                           INSERT INTO books (title,author,genre,is_available,borrowed_by_member_id)
                           VALUES(%s,%s,%s,%s,%s)
                        """
                val = (
                    data.title,
                    data.author,
                    data.genre,
                    data.is_available,
                    data.borrowed_by_member_id
                )
                cursor.execute(query,val)
                last_id = cursor.lastrowid
                conn.commit()
                return last_id
    def get_the_books(self):
        with get_connection() as conn:
            with conn.cursor(dictionary=True) as cursor:
                cursor.execute("SELECT * FROM books")
                data = cursor.fetchall()
                return data
    def get_by_id(self,id:int):
        with get_connection() as conn:
            with conn.cursor(dictionary=True) as cursor:
                query = "SELECT * FROM books WHERE id = %s"
                cursor.execute(query,(id,))

                by_id = cursor.fetchone()
                return by_id
    def update_by_id(self,id:int,data:dict):
        with get_connection() as conn:
            with conn.cursor(dictionary=True) as cursor:
                parts = []
                values = []
                for key,value in data.items() :
                    parts.append(f"{key} = %s")
                    values.append(value)
                values.append(id)
                query = f"UPDATE books SET {", ".join(parts)} WHERE id = %s"
                cursor.execute(query,values)
                conn.commit()
                is_change = cursor.rowcount > 0 
                return is_change

    def set_available(self,body:Ret_bro):
        with get_connection() as conn:
            with conn.cursor(dictionary=True) as cursor:
                book = self.get_by_id(body.id)
                member = members.get_by_id(body.member_id)
                if not book:
                    raise HTTPException(status_code=404,detail=f"book id {body.id} not found")
                if not member :
                        raise HTTPException(status_code=404,detail=f"member id {body.member_id} not found")
                if body.ret_bro == "borrow":
                   
                    if book["is_available"]== False:
                        raise HTTPException(status_code=400,detail="Book is already borrowed")
                    
                    if member ["is_activ"] == False:
                        raise HTTPException(status_code=400,detail="the member is not active")
                    if self.count_borrowed_books(body.member_id)>3:
                        raise HTTPException(status_code=400,detail="to the member have mor then 2 books")
                    data ={
                        "is_available":False,
                        "borrowed_by_member_id":body.member_id
                    }
                    self.update_by_id(body.id,data)
                    data_member={
                        "total_borrows":member["total_borrows"] + 1

                    }
                    members.patch_member(body.member_id,data_member)
                    return {"status": "success", "message": "Book borrowed successfully"}
                else:
                    if body.member_id != book["borrowed_by_member_id"]:
                        raise HTTPException(status_code=400,detail=f"the member {body.member_id} is not the ouner")
                    data ={
                        "is_available":True,
                        "borrowed_by_member_id":None
                    }
                    self.update_by_id(body.id,data)
                    

                    return {"status": "success", "message": "Book return  successfully"}

    def count_borrowed_books(self,id):
        with get_connection() as conn:
            with conn.cursor(dictionary=True) as cursor:
                query="SELECT COUNT(*) AS count_books FROM books WHERE borrowed_by_member_id = %s"
                cursor.execute(query,(id,))
                count = cursor.fetchone()
                return count["count_books"]
    def get_count_books(self):
         with get_connection() as conn:
            with conn.cursor(dictionary=True) as cursor:
                cursor.execute("SELECT COUNT(*) AS count_books FROM books")
                count = cursor.fetchone()
                return count
    def get_count_available_books(self):
         with get_connection() as conn:
            with conn.cursor(dictionary=True) as cursor:
                cursor.execute("SELECT COUNT(*) AS count_available FROM books WHERE is_available = True")
                count = cursor.fetchone()
                return count
    def get_count_not_available_books(self):
         with get_connection() as conn:
            with conn.cursor(dictionary=True) as cursor:
                cursor.execute("SELECT COUNT(*) AS count_not_available FROM books WHERE is_available = False")
                count = cursor.fetchone()
                return count
    def books_by_genre(self,genre):
        with get_connection() as conn:
            with conn.cursor(dictionary=True) as cursor:
                query = "SELECT genre, COUNT(*) AS count_books FROM books WHERE genre = %s"
                cursor.execute(query,(genre,))
                count = cursor.fetchone()
                return count
    def top_count(self):
         with get_connection() as conn:
            with conn.cursor(dictionary=True) as cursor:
                query = """
                SELECT id, name, email, total_borrows 
                FROM members 
                ORDER BY total_borrows DESC 
                LIMIT 1
                """
                cursor.execute(query)
                top_member = cursor.fetchone()
                
                return top_member


                    
                


