from pydantic import BaseModel
from typing import Optional
class AuthorBase(BaseModel):
    name: str
    email: str
    bio: Optional[str]

class AuthorCreate(AuthorBase):
    pass


class Author(AuthorBase):
    id: int

    class Config:
        orm_mode = True


##################################################3

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
    email: str
    password: str
    

class UserCreate(UserBase):
    pass


class User(BaseModel):
    name: str
    email: str
    id: int

    class Config:
        orm_mode = True