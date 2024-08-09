from pydantic import BaseModel, EmailStr
from typing import Optional


class PostBase(BaseModel):
    title: str
    content: str
    user_id: int
    category_id: int
    published: bool = True

class PostCreate(PostBase):
    pass


class Post(PostBase):
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

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: Optional[int] = None