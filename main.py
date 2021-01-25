from fastapi import FastAPI
from pydantic import BaseModel
from .routers import book, user, file

app = FastAPI()

app.include_router(book.router)
app.include_router(user.router)
app.include_router(file.router)

@app.get("/")
async def root():
    return {"message": "Hello World"}
