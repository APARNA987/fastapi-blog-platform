from Blog.database import Base, SessionLocal
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime
from datetime import datetime
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index = True)
    username = Column(String, nullable=False, unique=True)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)  # hashed password

    blogs = relationship("Blog", back_populates="owner")

class Blog(Base):
    __tablename__ = "blogs"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    published = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    owner_id = Column(Integer, ForeignKey("users.id")) #  This creates a foreign key, meaning: Each blog is linked to one user owner_id will store the user’s ID

    owner = relationship("User", back_populates="blogs")


# User has blogs: list of blogs that user wrote

# Blog has owner: the user who owns it