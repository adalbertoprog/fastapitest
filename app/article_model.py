from pydantic import BaseModel
from typing import Optional

class Article(BaseModel):
    title: str
    content: str
    published: bool = True
    length: Optional[int] = None