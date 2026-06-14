import uvicorn
from fastapi import FastAPI
from database.db.db_connection import get_connection
from logger import logger
from database.create_tables import create_the_tables

app = FastAPI()


@app.get("/")
def root():
    logger.info("GET / called")
    return {"message": "API is running"}


if __name__ == "__main__":
    logger.info("Starting server on http://127.0.0.1:8000")
    create_the_tables()
    uvicorn.run("main:app", port=8000, host="127.0.0.1", reload=True)
