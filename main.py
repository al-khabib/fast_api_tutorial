from fastapi import FastAPI
from fastapi import Body

app = FastAPI()


# path operation or root function
@app.get("/")
async def root():
    return {"message": "Welcome to my website!"}

@app.get("/about")
async def about():
    return {"message": "This is the about page of my website."}

@app.get("/posts")
async def get_posts():
    return {"message": "Here are all the posts on my website."}

@app.post("/posts")
async def create_post(payload: dict = Body(...)):
    print('payload: ', payload)
    return payload

