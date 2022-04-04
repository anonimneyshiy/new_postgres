from sqlalchemy import Column, String, Integer, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from database.utils_for_db import Base


class Post(Base):
    __tablename__ = "blog_posts"

    id = Column(Integer, primary_key=True, index=True, unique=True)
    title = Column(String)
    text = Column(String(length=350))
    date = Column(DateTime)
    user = Column(Integer, ForeignKey('blog_users.id'))
    user_id = relationship('User')


class User(Base):
    __tablename__ = "blog_users"

    id = Column(Integer, primary_key=True, index=True, unique=True)
    name = Column(String, unique=True)
    email = Column(String, unique=True)
    password = Column(String)
    date = Column(DateTime)
    is_active = Column(Boolean, default=False)
    is_admin = Column(Boolean, default=False)

