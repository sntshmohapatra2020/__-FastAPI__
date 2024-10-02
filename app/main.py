from fastapi import FastAPI
from . import models
from .database import engine
from .routers import books, users, authentication

app = FastAPI()

app.include_router(books.router)
app.include_router(users.router)
app.include_router(authentication.router)

models.Base.metadata.create_all(engine)
