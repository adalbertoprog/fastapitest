from typing import Optional
from fastapi import APIRouter, HTTPException, Response, status, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from .. import models, schemas


router = APIRouter()


@router.get("/categories", response_model=list[schemas.Category])
def loadCategories(db: Session = Depends(get_db)):
    categories = db.query(models.Category).all()
    return categories


@router.post("/categories", status_code=status.HTTP_201_CREATED, response_model=schemas.Category)
def addCategory(category: schemas.CategoryCreate, db: Session = Depends(get_db)):
    newCategory = models.Category(name=category.name, description=category.description)
    db.add(newCategory)
    db.commit()
    db.refresh(newCategory)
    return newCategory


@router.get("/categories/{id}", response_model=schemas.Category)
def loadCategory(id: int, db: Session = Depends(get_db)):
    category = db.query(models.Category).filter(models.Category.id == id).first()
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    else:
        return category


@router.put("/categories/{id}", response_model=schemas.Category)
def updateCategory(id: int, category: schemas.ArticleCreate, db: Session = Depends(get_db)):
    uCategory = db.query(models.Category).filter(models.Category.id == id)
    if not uCategory.first():
        raise HTTPException(status_code=404, detail="Category not found")
    else:
        uCategory.update(category.dict())
        db.commit()
        return category

@router.delete("/categories/{id}", status_code=status.HTTP_204_NO_CONTENT)
def deleteCategory(id: int, db: Session = Depends(get_db)):
    category = db.query(models.Category).filter(models.Category.id == id)
    if category.first() == None:
        raise HTTPException(status_code=404, detail="Category not found")
    else:
        category.delete()
        db.commit()
        return Response(status_code=status.HTTP_204_NO_CONTENT)