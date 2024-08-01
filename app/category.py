from fastapi import APIRouter
from app.data import listCategory

router = APIRouter()

@router.get("/categories")
def getCategories():
    return {"data": listCategory}

@router.get("/categories/{id}")
def getCategory(id: int):
    for category in listCategory:
        if category.id == id:
            return {"data": category}
    return {"message": "Category not found"}

@router.post("/categories")
def createCategory(category: dict):
    listCategory.append(category)
    return {"data": category}

@router.put("/categories/{id}")
def updateCategory(id: int, category: dict):
    for i in range(len(listCategory)):
        if listCategory[i].id == id:
            listCategory[i] = category
            return {"data": category}
    return {"message": "Category not found"}

@router.delete("/categories/{id}")
def deleteCategory(id: int):
    for i in range(len(listCategory)):
        if listCategory[i].id == id:
            listCategory.pop(i)
            return {"message": "Category deleted"}
    return {"message": "Category not found"}


