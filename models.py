from sqlmodel import SQLModel, Field


class Link(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    original_url: str
    short_name: str = Field(unique=True)