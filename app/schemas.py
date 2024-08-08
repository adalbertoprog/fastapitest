from pydantic import BaseModel, EmailStr
from typing import Optional


class ArticleBase(BaseModel):
    title: str
    content: str
    author_id: int
    category_id: str
    published: bool = True

class ArticleCreate(ArticleBase):
    pass


class Article(ArticleBase):
    id: int

    class Config:
        orm_mode = True

###############################################3

class CategoryBase(BaseModel):
    name: str
    description: Optional[str]
    

class CategoryCreate(CategoryBase):
    pass


class Category(CategoryBase):
    id: int

    class Config:
        orm_mode = True

##################################################

class UserBase(BaseModel):
    name: str
    email: EmailStr
    password: str
    

class UserCreate(UserBase):
    pass


class User(BaseModel):
    name: str
    email: EmailStr
    id: int

    class Config:
        orm_mode = True

class UserLogin(BaseModel):
    email: EmailStr
    password: str