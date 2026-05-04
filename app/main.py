from fastapi import FastAPI
from app.api.auth import router as auth_api
from app.db.database import Base, Engine
from app.models import user  # noqa: F401  # ensure model registration with Base.metadata

app = FastAPI()
app.include_router(auth_api)

@app.on_event("startup")
def create_database_tables() -> None:
    Base.metadata.create_all(bind=Engine)

@app.get("/")
def root():
    return {"message": "wellcome to my api"}

