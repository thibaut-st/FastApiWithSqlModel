from sqlmodel import Field, SQLModel


class Hero(SQLModel, table=True):
    """Hero model."""

    id: int | None = Field(default=None, primary_key=True)
    name: str
    secret_name: str
    age: int | None = None
