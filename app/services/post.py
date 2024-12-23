from sqlalchemy.orm import Session
from app.cruds.post import get_posts, create_post
from app.schemas.post import PostCreate

def fetch_posts(db: Session):
    return get_posts(db)

def add_post(db: Session, post_data: PostCreate):
    return create_post(db, post_data)