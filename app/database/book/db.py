from database.db.db_connection import get_connection
from models.book.modle import create_book
class Book():
    def create_book(self,data:create_book):
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



