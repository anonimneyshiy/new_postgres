from sqlalchemy import Column, String, Integer, Text, DateTime

from database.utils_for_db import Base


class Post(Base):
    __tablename__ = "blog_posts"

    id = Column(Integer, primary_key=True, index=True, unique=True)
    title = Column(String)
    text = Column(Text(350))
    date = Column(DateTime)
