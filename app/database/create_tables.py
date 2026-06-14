
from database.db.db_connection import get_connection
def create_the_tables():
    with get_connection() as conn:
        with conn.cursor(dictionary=True) as cursor:
            query_books = """
                    CREATE TABLE IF NOT EXISTS books(
                    id INT PRIMAY KEY AUTO_INCREMENT,
                    title VARCHAR(50) NOT NULL,
                    author VARCHAR(50) NOT NULL,
                    genre ENUM('Fiction','Non-Fiction','Science','Other') NOT NULL,
                    is_available BOOLEAN NOT NULL,
                    borrowed_by_member_id  INT

                    )

                    """
            cursor.execute(query_books)
            conn.commit()
            query_members = """
                    CREATE TABLE IF NOT EXISTS members(
                    id INT PRIMARY KEY AUTO_INCREMENT,
                    name VARCHAR(50) NOT NULL,
                    email VARCHAR(50) UNIQUE,
                    is_activ BOOLEAN NOT NULL,
                    total_borrows INT
                        )
                            """
            cursor.execute(query_members)
            conn.commit()