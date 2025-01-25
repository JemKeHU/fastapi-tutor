from fastapi import FastAPI

my_tutorial_app = FastAPI()

@my_tutorial_app.get("/")
async def root():
    return {"message": "Hello from FastAPI!"}