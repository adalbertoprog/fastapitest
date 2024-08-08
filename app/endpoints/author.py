from typing import Optional
from fastapi import APIRouter, HTTPException, Response, status, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from .. import models, schemas


router = APIRouter(
    prefix="/authors",
    tags = ["Authors"],
)



@router.get("/", response_model=list[schemas.Author])
def read_authors(db: Session = Depends(get_db)):
    authors = db.query(models.Author).all()
    return authors


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.Author)
def create_author(author: schemas.AuthorCreate, db: Session = Depends(get_db)):
    new_author = models.Author(name=author.name, email=author.email, bio=author.bio)
    db.add(new_author)
    db.commit()
    db.refresh(new_author)
    return new_author


@router.get("/{id}", response_model=schemas.Author)
def read_author(id: int, db: Session = Depends(get_db)):
    author = db.query(models.Author).filter(models.Author.id == id).first()
    if author == None:
        raise HTTPException(status_code=404, detail="Author not found")
    else:
        return author


@router.put("/{id}", response_model=schemas.Author)
def update_author(id: int, author: schemas.AuthorCreate, db: Session = Depends(get_db)):
    db_author = db.query(models.Author).filter(models.Author.id == id)
    if not db_author.first():
        raise HTTPException(status_code=404, detail="Author not found")
    else:
        db_author.update(author.dict())
        db.commit()
        return author

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_author(id: int, db: Session = Depends(get_db)):
    db_author = db.query(models.Author).filter(models.Author.id == id)
    if db_author.first() == None:
        raise HTTPException(status_code=404, detail="Author not found")
    else:
        db_author.delete()
        db.commit()
        return Response(status_code=status.HTTP_204_NO_CONTENT)