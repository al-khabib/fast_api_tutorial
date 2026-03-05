from fastapi import FastAPI

app = FastAPI()


# path operation or root function
@app.get("/")
async def root():
    return {"message": "Hello World"}

