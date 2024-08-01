from fastapi import FastAPI
from app.category import router as category_router


app = FastAPI()

app.include_router(category_router)

@app.get("/")
def read_root():
    return {"Hello": "Hey Adalberto, how are you?"} 
