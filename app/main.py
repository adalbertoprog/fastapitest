from fastapi import FastAPI

from controller import *

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "Hey Adalberto, how are you?"} 