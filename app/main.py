from fastapi import FastAPI
from app.author import router as author_router


app = FastAPI()

app.include_router(author_router)

@app.get("/")
def read_root():
    return {"Hello": "Hey Adalberto, how are you?"} 
