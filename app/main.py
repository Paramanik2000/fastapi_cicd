from fastapi import FastAPI
from app.database import engine
from app import models
from fastapi.middleware.cors import CORSMiddleware

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="FastAPI CI/CD Project")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # later we restrict this
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "FastAPI + Docker + GitHub Actions 🚀"}

@app.get("/health")
def health():
    return {"status": "ok"}
