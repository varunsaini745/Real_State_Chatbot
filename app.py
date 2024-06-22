from fastapi import FastAPI, HTTPException, APIRouter, status, Depends
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from pydantic import BaseModel

from typing import ClassVar
from dotenv import load_dotenv
from pydantic import BaseModel
from qa_processor import QAProcessor

load_dotenv()
class Model(BaseModel):
    a: ClassVar[str]

app = FastAPI(title = "Real State Based Question Answering System", version = "0.0.1")
prefix_router = APIRouter(prefix="/api")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

    
    
class Item(BaseModel):
   question: str

   

@prefix_router.get("/")
async def root():
    return {"message": "Server running correctly"}

@prefix_router.post("/question_answering_system")
async def identify_risk(req: Item):
    res = QAProcessor().ask_question(req.question)
    return res


app.include_router(prefix_router)
if __name__ == "__main__":
    uvicorn.run('app:app', reload=True)