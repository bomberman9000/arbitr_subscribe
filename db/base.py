import os
from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise ValueError("DATABASE_URL не указан в .env")

engine = create_async_engine(DATABASE_URL, echo=False)

# Асинхронная сессия
AsyncSessionLocal = async_sessionmaker(engine, expire_on_commit=False)
