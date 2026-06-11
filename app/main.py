import uvicorn
from fastapi import FastAPI
from app.database.db_connection import get_connection
from app.logger import logger

app = FastAPI()


@app.get("/")
def root():
    logger.info("GET / called")
    return {"message": "API is running"}


if __name__ == "__main__":
    logger.info("Starting server on http://127.0.0.1:8000")
    uvicorn.run("app.main:app", port=8000, host="127.0.0.1", reload=True)
