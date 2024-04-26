from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

from src.settings import SQLITE_ACCESS

async_engine = create_async_engine(SQLITE_ACCESS, echo=True)

connection = async_engine.connect()

AsyncSession = async_sessionmaker(bind=async_engine)
