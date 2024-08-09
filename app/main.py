from fastapi import FastAPI
from app import models

from app.endpoints.post import router as post_router
from app.endpoints.user import router as user_router
from app.endpoints.auth import router as auth_router
from app.database import engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(post_router)
app.include_router(user_router)
app.include_router(auth_router)


