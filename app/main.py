from fastapi import FastAPI
from app.endpoints.author import router as author_router


app = FastAPI()

app.include_router(category_router)

@app.get("/")
def read_root():
    return {"Hello": "Hey Adalberto, how are you?"} 
