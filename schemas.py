from sqlmodel import SQLModel


class LinkCreate(SQLModel):
    original_url: str
    short_name: str

class LinkUpdate(SQLModel):
    original_url: str
    short_name: str