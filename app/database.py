from urllib.parse import quote_plus
from app.config import Settings, get_settings
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

settings = get_settings()

encoded_password = quote_plus(settings.DATABASES_PASSWORD)

DATABASE_URL = (
    f"postgresql://{settings.DATABASES_USER}:"
    f"{encoded_password}"
    f"@localhost:5432/{settings.DATABASES_NAME}"
)

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(bind=engine)

class Base(DeclarativeBase):
    pass


def get_db():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()