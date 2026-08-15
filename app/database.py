import os
from dotenv import load_dotenv
from sqlmodel import SQLModel, Session, create_engine


load_dotenv()

database_url = os.getenv("DATABASE_URL")

if os.getenv("TESTING") == "1":
    database_url = "sqlite:///test.db"

elif database_url is None:
    database_url = "sqlite:///test.db"

elif database_url.startswith("postgres://"):
    database_url = database_url.replace(
        "postgres://",
        "postgresql+psycopg://",
        1,
    )
elif database_url.startswith("postgresql://"):
    database_url = database_url.replace(
        "postgresql://",
        "postgresql+psycopg://",
        1,
    )

if (
    "sslmode=" not in database_url
    and database_url.startswith("postgresql+psycopg://")
):
    separator = "&" if "?" in database_url else "?"
    database_url += f"{separator}sslmode=require"

engine = create_engine(database_url)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session