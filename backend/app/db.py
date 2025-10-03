from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.orm import declarative_base
import os

# Import DATABASE_URL from environment variable
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql+psycopg://postgres:postgres@localhost:5432/eduapp")

# Create async engine with echo=True
engine = create_async_engine(
    DATABASE_URL,
    echo=True,
    future=True,
)

# Create Base declarative base
Base = declarative_base()

# Create sessionmaker that yields AsyncSession
AsyncSessionLocal = async_sessionmaker(
    engine,
    class_=AsyncSession,
    expire_on_commit=False,
)


async def get_db():
    """FastAPI dependency to get database session"""
    async with AsyncSessionLocal() as session:
        try:
            yield session
        finally:
            await session.close()
