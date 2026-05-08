from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.core.config import settings
from sqlalchemy.orm import DeclarativeBase

DB_url=settings.DATABASE_URL


Engine=create_engine(DB_url)

session_local = sessionmaker(autocommit=False,autoflush=False,bind=Engine)


class Base(DeclarativeBase):
    pass

