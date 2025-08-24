from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


SQLALCHEMY_DATABASE_URL = "sqlite:///./Blog.db"

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args = {"check_same_thread": False})

SessionLocal = sessionmaker(bind = engine, autocommit = False, autoflush = False)
Base = declarative_base()


def get_db(): #This function gives you a connection to the database (called db) every time you need it in your API route.
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()