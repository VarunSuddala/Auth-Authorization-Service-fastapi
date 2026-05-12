from fastapi import FastAPI
from app.api.auth import router as auth_api
from app.db.database import Base, Engine
from app.models import user
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(auth_api)
@asynccontextmanager
async def lifespan(app:FastAPI):
    Base.metadata.create_all(bind=Engine)
    yield

@app.get("/")
def root():
    return {"message": "welcome to my api"}

