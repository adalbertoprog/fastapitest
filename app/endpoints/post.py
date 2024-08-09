from typing import Optional
from fastapi import APIRouter, HTTPException, Response, status, Depends
from sqlalchemy.orm import Session

from app import oauth2
from app.database import get_db
from .. import models, schemas


router = APIRouter(
    prefix="/posts",
    tags = ["Posts"],
)


@router.get("/", response_model=list[schemas.Post])
def read_posts(db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    posts = db.query(models.Post).filter(models.Post.user_id == current_user.id).all()
    print(current_user.email)
    return posts


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.Post)
def create_post(post: schemas.PostCreate, db: Session = Depends(get_db), 
                   current_user: int = Depends(oauth2.get_current_user)):
    print(current_user.email)
    new_post = models.Post(title=post.title, content=post.content, user_id=current_user.id, category_id=post.category_id, published=post.published)
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post


@router.get("/{id}", response_model=schemas.Post)
def read_post(id: int, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    post = db.query(models.Post).filter(models.Post.id == id).first()
    if post == None:
        raise HTTPException(status_code=404, detail="Post not found")
    else:
        return post
    

@router.put("/{id}", response_model=schemas.Post)
def update_post(id: int, post: schemas.PostCreate, db: Session = Depends(get_db), 
                   current_user: int = Depends(oauth2.get_current_user)):
    db_post = db.query(models.Post).filter(models.Post.id == id)
    if not db_post.first():
        raise HTTPException(status_code=404, detail="Post not found")
    else:
        if db_post.first().user_id != current_user.id:
            raise HTTPException(status_code=403, detail="Not authorized to perform requested action")
        db_post.update(post.dict())
        db.commit()
        return post

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    db_post = db.query(models.Post).filter(models.Post.id == id)
    if db_post.first() == None:
        raise HTTPException(status_code=404, detail="Post not found")
    else:
        if db_post.first().user_id != current_user.id:
            raise HTTPException(status_code=403, detail="Not authorized to perform requested action")
        db_post.delete()
        db.commit()
        return Response(status_code=status.HTTP_204_NO_CONTENT)