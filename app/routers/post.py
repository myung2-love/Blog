from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.post import Post, PostCreate
from app.services.post import fetch_posts, add_post
from app.db import get_db

router = APIRouter(
    prefix="/posts",
    tags=["Posts"]
)

@router.get("/", response_model=list[Post])
def get_posts_endpoint(db: Session = Depends(get_db)):
    return fetch_posts(db)

@router.post("/", response_model=Post)
def create_post_endpoint(post: PostCreate, db: Session = Depends(get_db)):
    return add_post(db, post)