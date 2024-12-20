import time
from sqlalchemy.exc import OperationalError
from fastapi import FastAPI
from app.routers import post
from app.db import engine, Base

app = FastAPI()

def initialize_database():
    retries = 5
    for attempt in range(retries):
        try:
            print(f"Attempting to initialize the database (Attempt {attempt + 1})...")
            Base.metadata.create_all(bind=engine)
            print("Database initialized successfully.")
            break
        except OperationalError as e:
            print(f"Database initialization failed: {e}. Retrying in 5 seconds...")
            time.sleep(5)
    else:
        raise RuntimeError("Failed to initialize the database after multiple attempts.")

# DB 초기화
initialize_database()

# 라우터 등록
app.include_router(post.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Blog API!"}