my_articles = [
    {"title": "title of article 1", "content": "content of article 1", "id": 1},
    {"title": "title of article 2", "content": "content of article 2", "id": 2}
]

authors = [
    {"name": "author 1", "email": "email 1", "id": 1},
    {"name": "author 2", "email": "email 2", "id": 2},
    {"name": "author 3", "email": "email 3", "id": 3},
]

def find_article(id):
    for p in my_articles:
        if p["id"] == id:
            return p
        
def find_article_index(id):
    for i, p in enumerate(my_articles):
        if p['id'] == id:
            return i