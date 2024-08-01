from app.category_model import CategoryModel

my_articles = [
    {"title": "title of article 1", "content": "content of article 1", "id": 1},
    {"title": "title of article 2", "content": "content of article 2", "id": 2}
]

listCategory = [
    CategoryModel(id=1, name="category 1"),
    CategoryModel(id=2, name="category 2"),
    CategoryModel(id=3, name="category 3"),
]

def find_article(id):
    for p in my_articles:
        if p["id"] == id:
            return p
        
def find_article_index(id):
    for i, p in enumerate(my_articles):
        if p['id'] == id:
            return i