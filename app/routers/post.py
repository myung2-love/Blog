from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.post import Post, PostCreate
from app.crud.post import get_posts, create_post
from app.db import get_db

router = APIRouter(
    prefix="/posts",
    tags=["Posts"]
)

@router.get("/", response_model=list[Post])
def get_posts_endpoint(db: Session = Depends(get_db)):
    return get_posts(db)

@router.post("/", response_model=Post)
def create_post_endpoint(post: PostCreate, db: Session = Depends(get_db)):
    return create_post(db, post)