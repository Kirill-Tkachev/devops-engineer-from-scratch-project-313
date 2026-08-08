from sqlmodel import SQLModel, Session, create_engine
from dotenv import load_dotenv
import os


load_dotenv()

database_url = os.getenv("DATABASE_URL")

if database_url is None:
    database_url = "sqlite:///test.db"
else:
    database_url = database_url.replace(
        "postgresql://",
        "postgresql+psycopg://",
        1,
    )

    if "sslmode=" not in database_url:
        separator = "&" if "?" in database_url else "?"
        database_url += f"{separator}sslmode=require"


engine = create_engine(database_url)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session