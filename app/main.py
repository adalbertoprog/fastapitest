import random
from typing import Optional, Union

from fastapi import FastAPI, Response, status, HTTPException
from fastapi.params import Body
from pydantic import BaseModel

app = FastAPI()


# variables
my_articles = [{"title": "title of article 1", "content": "content of article 1", "id": 1},
    {"title": "title of article 2", "content": "content of article 2", "id": 2}]

#functions
def find_article(id):
    for p in my_articles:
        if p["id"] == id:
            return p
        
def find_article_index(id):
    for i, p in enumerate(my_articles):
        if p['id'] == id:
            return i

class Article(BaseModel):
    title: str
    content: str
    published: bool = True
    length: Optional[int] = None


@app.get("/")
def read_root():
    return {"Hello": "Hey Adalberto, how are you?"} 


@app.post("/articlesdd")
def create_articles(article: dict = Body(...)):
    print(article)
    return {"new_item": f"title: {article['title']} content: {article['content']}"}

# using data from variable
@app.get("/articles")
def get_articles():
    return {"data": my_articles}

# using Paydantic
@app.post("/postsa")
def create_new_article(article: Article):
    print(article)
    return {"post": "new post has been created"}


# using Paydantic
@app.post("/posts_pydantic")
def new_article_pydantic(article: Article):
    print(article.dict())
    return {"data": article}

# using Paydantic and variables
@app.post("/posts", status_code=status.HTTP_201_CREATED)
def new_article_pydantic(article: Article):
    new_article = article.dict()
    new_article['id'] = random.randrange(0, 1000000)
    my_articles.append(new_article)
    return {"data": new_article}

# Get a post by id 
@app.get("/posts/{id}")
def get_article(id: int, response: Response):
    print(id)
    #find_posts = next((post for post in my_posts if post["id"] == id), None)
    if not find_article(id):
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"message": "post not found"}
    else:
        return {"data": find_article(id)}

# using HTTP Exception
@app.get("/postshttp/{id}") 
def get_article(id: int):
    post = find_article(id)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="post not found")
    else:
        print(find_article_index(id))
        return {"data": post}
 
 #deleting a post
@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_article(id: int):
    index = find_article_index(id)
    my_articles.pop(index)
    print(index)
    #return {"message": "post deleted"}
    if not index:
         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="post not found")
    else:
        my_articles.pop(index)
        return {"message": "article deleted"}