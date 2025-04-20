# app/api.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routers.ParsingCVs import router as ParsingCVsRouter
from app.api.routers.GetAllCandidaData import router as GetAllCandidaDataRouter
from app.api.routers.GetDataByCandidaId import router as GetDataByCandidaIdRouter

from app.api.routers.Test import router as TestRouter

app = FastAPI()

origins = [
    "http://localhost:3000",
    "localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Explicitly allowing only localhost:3000
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# Include the routers
app.include_router(ParsingCVsRouter, prefix="/api/v1", tags=["CV Parser"])
app.include_router(GetAllCandidaDataRouter, tags=["Get data"])
app.include_router(GetDataByCandidaIdRouter, tags=["Get data"])

app.include_router(TestRouter)

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI app!"}
