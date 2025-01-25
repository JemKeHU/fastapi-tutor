from fastapi import FastAPI
from fastapi.responses import FileResponse

my_tutorial_app = FastAPI()

@my_tutorial_app.get("/")
def root():
    return FileResponse("public/index.html")