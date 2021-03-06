from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session

from app.config import PG_URL


SQLALCHEMY_DATABASE_URL = PG_URL

engine = create_engine(SQLALCHEMY_DATABASE_URL)

Base = declarative_base()


def connect_db():
    session = Session(bind=engine)
    return session
