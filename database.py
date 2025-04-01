# database.py
import os
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from base import Base  # Import Base from base.py

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql+asyncpg://postgres:helloworld@localhost/uvicorn2")

engine = create_async_engine(DATABASE_URL, echo=True)

# Asynchronous session maker
async_session_maker = sessionmaker(
    bind=engine, class_=AsyncSession, expire_on_commit=False
)

# Utility function to get DB session
async def get_db():
    async with async_session_maker() as session:
        yield session
