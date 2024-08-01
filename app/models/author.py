from pydantic import BaseModel
from typing import Optional

class Author(BaseModel):
    id: int
    name: str
    email: str
    bio: Optional[str] = None