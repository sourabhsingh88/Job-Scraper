from fastapi import FastAPI
from data_action import router as data_router 

app = FastAPI(title="Job Scraper")

from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # sab allow, chahe to apna domain daal do
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root() :
    return {"message" : "welcome to job scrapper"}

app.include_router(data_router)

