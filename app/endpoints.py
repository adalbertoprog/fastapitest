import random
from fastapi import Response, status, HTTPException, Body
from app.article_model import Article
from app.data import my_articles, find_article, find_article_index



@app.post("/articlesdd")
def create_articles(article: dict = Body(...)):
    print(article)
    return {"new_item": f"title: {article['title']} content: {article['content']}"}

@app.get("/articles")
def get_articles():
    return {"data": my_articles}

@app.post("/postsa")
def create_new_article(article: Article):
    print(article)
    return {"post": "new post has been created"}

@app.post("/posts_pydantic")
def new_article_pydantic(article: Article):
    print(article.dict())
    return {"data": article}

@app.post("/posts", status_code=status.HTTP_201_CREATED)
def new_article_pydantic(article: Article):
    new_article = article.dict()
    new_article['id'] = random.randrange(0, 1000000)
    my_articles.append(new_article)
    return {"data": new_article}

@app.get("/posts/{id}")
def get_article(id: int, response: Response):
    print(id)
    if not find_article(id):
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"message": "post not found"}
    else:
        return {"data": find_article(id)}

@app.get("/postshttp/{id}") 
def get_article(id: int):
    post = find_article(id)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="post not found")
    else:
        print(find_article_index(id))
        return {"data": post}

@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_article(id: int):
    index = find_article_index(id)
    if not index:
         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="post not found")
    else:
        my_articles.pop(index)
        return {"message": "article deleted"}