from datetime import datetime

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database.utils_for_db import connect_db
from database.db_connector import get_post, add_post
from app.schemas import PostCreate

router = APIRouter()


@router.get("/get_post/")
def post_list(database: Session = Depends(connect_db)) -> dict:
    posts = get_post(database=database)
    return {'posts': posts}


@router.post("/create_post/")
def create_post(item: PostCreate, database: Session = Depends(connect_db)) -> str:
    current_post = add_post(
        database=database,
        item=item
    )
    return current_post
