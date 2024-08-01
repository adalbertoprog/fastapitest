from fastapi import APIRouter

router = APIRouter()

@router.get("/authors")
def read_authors():
    return {"message": "Hello from Module 1"}
