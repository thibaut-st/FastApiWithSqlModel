from fastapi import FastAPI

from src.database.helpers import add_and_commit
from src.models import Hero

app = FastAPI()


@app.get("/")
async def root() -> dict[str, str]:
    """
    Test your FastAPI endpoints.

    :return: Message
    """
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str) -> dict[str, str]:
    """
    Test your FastAPI endpoints.

    :param name: Name
    :return: Message
    """
    return {"message": f"Hello {name}"}


@app.post("/heroes")
async def create_heroes() -> list[Hero]:
    """Create heroes."""
    hero_1 = Hero(name="Deadpond", secret_name="Dive Wilson")  # noqa: S106
    hero_2 = Hero(name="Spider-Boy", secret_name="Pedro Parqueador")  # noqa: S106
    hero_3 = Hero(name="Rusty-Man", secret_name="Tommy Sharp", age=48)  # noqa: S106

    await add_and_commit([hero_1, hero_2, hero_3])

    return [hero_1, hero_2, hero_3]
