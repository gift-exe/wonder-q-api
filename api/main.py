from fastapi import FastAPI,Depends,Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware import Middleware








middleware = [
    Middleware(
        CORSMiddleware,
        allow_origins=['*'],
        allow_credentials=True,
        allow_methods=['*'],
        allow_headers=['*']
    )
]

app = FastAPI(title="Wonder Q api",
              middleware=middleware,
              description="save some stress my gee",
              version="1.0.0",
              
              )



@app.get("/")
def get_home():
    return {"you dey homepage, wetin you dey find for here? "}

