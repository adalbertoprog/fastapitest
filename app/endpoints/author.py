from fastapi import APIRouter, HTTPException, status
from app.core.data import authors
from app.models.author import Author

router = APIRouter()

def find_author(id):
    for author in authors:
        if author["id"] == id:
            return author

@router.get("/authors")
def read_authors():
    return {"data": authors}


@router.get("/authors/{id}")
def read_author(id: int):
    if not find_author(id):
        raise HTTPException(status_code=404, detail="Author not found")
    else:
        return {"data": find_author(id)}
    

#create author with Pydantic
@router.post("/authors", status_code=status.HTTP_201_CREATED)
def create_author(author: Author):
    new_author = author.dict()
    new_author["id"] = len(authors) + 1
    authors.append(new_author)
    return {"data": new_author}



#delete author
@router.delete("/authors/{id}")
def delete_author(id: int):
    index = find_author(id)
    if not index:
        raise HTTPException(status_code=404, detail="Author not found")
    else:
        authors.pop(index)
        return {"message": "Author deleted"}