from typing import Optional
from fastapi import APIRouter, HTTPException, Response, status, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from .. import models, schemas


router = APIRouter()


@router.get("/users", response_model=list[schemas.User])
def read_users(db: Session = Depends(get_db)):
    users = db.query(models.User).all()
    return users

@router.post("/users", status_code=status.HTTP_201_CREATED, response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = models.User(name=user.name, email=user.email, password=user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


@router.get("/users/{id}", response_model=schemas.User)
def read_user(id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if user == None:
        raise HTTPException(status_code=404, detail="User not found")
    else:
        return user
    

@router.put("/users/{id}", response_model=schemas.User)
def update_user(id: int, user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(models.User).filter(models.User.id == id)
    if not db_user.first():
        raise HTTPException(status_code=404, detail="User not found")
    else:
        db_user.update(user.dict())
        db.commit()
        return user

@router.delete("/users/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(id: int, db: Session = Depends(get_db)):
    db_user = db.query(models.User).filter(models.User.id == id)
    if db_user.first() == None:
        raise HTTPException(status_code=404, detail="User not found")
    else:
        db_user.delete()
        db.commit()
        return Response(status_code=status.HTTP_204_NO_CONTENT)