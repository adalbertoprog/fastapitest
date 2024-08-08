from typing import Optional
from fastapi import APIRouter, HTTPException, Response, status, Depends
from sqlalchemy.orm import Session

from app import oauth2
from app.database import get_db
from .. import models, schemas


router = APIRouter(
    prefix="/articles",
    tags = ["Articles"],
)



@router.get("/", response_model=list[schemas.Article])
def read_articles(db: Session = Depends(get_db), get_current_user: int = Depends(oauth2.get_current_user)):
    articles = db.query(models.Article).all()
    return articles


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.Article)
def create_article(article: schemas.ArticleCreate, db: Session = Depends(get_db), 
                   get_current_user: int = Depends(oauth2.get_current_user)):
    new_article = models.Article(title=article.title, content=article.content, author=article.author, category=article.category, published=article.published)
    db.add(new_article)
    db.commit()
    db.refresh(new_article)
    return new_article


@router.get("/{id}", response_model=schemas.Article)
def read_article(id: int, db: Session = Depends(get_db)):
    article = db.query(models.Article).filter(models.Article.id == id).first()
    if article == None:
        raise HTTPException(status_code=404, detail="Article not found")
    else:
        return article
    

@router.put("/{id}", response_model=schemas.Article)
def update_article(id: int, article: schemas.ArticleCreate, db: Session = Depends(get_db)):
    db_article = db.query(models.Article).filter(models.Article.id == id)
    if not db_article.first():
        raise HTTPException(status_code=404, detail="Article not found")
    else:
        db_article.update(article.dict())
        db.commit()
        return article

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_article(id: int, db: Session = Depends(get_db)):
    db_article = db.query(models.Article).filter(models.Article.id == id)
    if db_article.first() == None:
        raise HTTPException(status_code=404, detail="Article not found")
    else:
        db_article.delete()
        db.commit()
        return Response(status_code=status.HTTP_204_NO_CONTENT)