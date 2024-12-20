from sqlalchemy.orm import Session
from app.models.post import Post
from app.schemas.post import PostCreate

def get_posts(db: Session):
    return db.query(Post).all()

def create_post(db: Session, post: PostCreate):
    db_post = Post(**post.dict())
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post