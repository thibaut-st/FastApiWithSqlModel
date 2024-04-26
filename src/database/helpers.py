from sqlmodel import SQLModel

from src.database.engine import AsyncSession


async def add_and_commit(data: list[SQLModel]) -> None:
    """
    Add data and commit to database.

    :param data: Models to add
    """
    async with AsyncSession() as async_session:
        async_session.add_all(data)
        await async_session.flush()
        await async_session.commit()
        [await async_session.refresh(d) for d in data]  # type: ignore[func-returns-value]
