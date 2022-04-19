from datetime import datetime

from sqlalchemy.orm import Session

from database.models import Post
from app.schemas import PostCreate


def get_post(database: Session) -> list:
    return database.query(Post).all()


def add_post(
    database: Session,
    item: PostCreate
) -> Post:
    post = Post(
        id=1,
        **item.dict()
    )
    database.add(post)
    database.commit()

    return post
