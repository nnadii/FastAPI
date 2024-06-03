from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Post(BaseModel):
    title: str
    content: str


@app.get("/")
def root():
    return {"message": "Welcome"}


@app.post("/posts")
def create_posts(post: Post):
    print(post.title)
    return {"data": "successful"}
