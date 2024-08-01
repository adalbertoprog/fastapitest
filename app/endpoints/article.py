import random
from fastapi import APIRouter, FastAPI, Response, status, HTTPException, Body
from app.models.article_model import Article
from app.core.data import my_articles


router = APIRouter()


def find_article(id):
    for p in my_articles:
        if p["id"] == id:
            return p
        
def find_article_index(id):
    for i, p in enumerate(my_articles):
        if p['id'] == id:
            return i
        
@router.post("/articlesdd")
def create_articles(article: dict = Body(...)):
    print(article)
    return {"new_item": f"title: {article['title']} content: {article['content']}"}

@router.get("/articles")
def get_articles():
    return {"data": my_articles}

@router.post("/postsa")
def create_new_article(article: Article):
    print(article)
    return {"post": "new post has been created"}

@router.post("/posts_pydantic")
def new_article_pydantic(article: Article):
    print(article.dict())
    return {"data": article}

@router.post("/posts", status_code=status.HTTP_201_CREATED)
def new_article_pydantic(article: Article):
    new_article = article.dict()
    new_article['id'] = random.randrange(0, 1000000)
    my_articles.append(new_article)
    return {"data": new_article}

@router.get("/posts/{id}")
def get_article(id: int, response: Response):
    print(id)
    if not find_article(id):
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"message": "post not found"}
    else:
        return {"data": find_article(id)}

@router.get("/postshttp/{id}") 
def get_article(id: int):
    post = find_article(id)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="post not found")
    else:
        print(find_article_index(id))
        return {"data": post}

@router.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_article(id: int):
    index = find_article_index(id)
    if not index:
         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="post not found")
    else:
        my_articles.pop(index)
        return {"message": "article deleted"}