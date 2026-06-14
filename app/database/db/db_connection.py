import mysql.connector

def get_connection():
    conn = mysql.connector.connect(
        host="localhost",
        port="3306",
        password="root",
        user="root",
        database="library_db"
    )
    return conn
