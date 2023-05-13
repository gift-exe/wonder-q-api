from fastapi import FastAPI,Depends,Request,Body,UploadFile,File
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware import Middleware
from .schemas import PassageModel
from .worker import processPassage,processLongPassage,processDocumentPassage








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


@app.post("/api/v1/process-short-passage")
async def process_passage(passage: PassageModel):
    response = await processPassage(str(passage.body))
    return response



@app.post("/api/v1/process-long-passage")
async def process_long_passage(passage: PassageModel):
    response = await processLongPassage(str(passage.body))
    return response



@app.post("/api/v1/process-pdf-passage")
async def process_long_passage(file: UploadFile = File(...)):
    filename = file.filename
    ext = filename.split(".")[1]
    if ext not in ['txt','pdf']:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail="File not allowed")
    file_content= await file.read()
    response = await processDocumentPassage(file_content)
    return response
