from app.models.category_model import CategoryModel

my_articles = [
    {"title": "title of article 1", "content": "content of article 1", "id": 1},
    {"title": "title of article 2", "content": "content of article 2", "id": 2}
]

authors = [
    {"name": "author 1", "email": "email 1", "id": 1},
    {"name": "author 2", "email": "email 2", "id": 2},
    {"name": "author 3", "email": "email 3", "id": 3},
]

listCategory = [
    CategoryModel(id=1, name="category 1"),
    CategoryModel(id=2, name="category 2"),
    CategoryModel(id=3, name="category 3"),
]
