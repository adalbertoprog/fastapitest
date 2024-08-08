from .database import Base

from sqlalchemy import TIMESTAMP, Boolean, Column, Integer, String, func


class Article(Base):
    __tablename__ = "articles"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    content = Column(String)
    user_id = Column(Integer)
    category_id = Column(Integer)
    published = Column(Boolean, default=True)
    #created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=func.now())

class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String, nullable=True)
    #created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=func.now())

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String, unique=True)
    password = Column(String)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=func.now())
