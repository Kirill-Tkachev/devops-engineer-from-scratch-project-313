from sqlmodel import SQLModel, create_engine
from dotenv import load_dotenv
import os

from models import Link

load_dotenv()

database_url = os.getenv("DATABASE_URL")

engine = create_engine(
    database_url.replace("postgresql://", "postgresql+psycopg://")
)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)



from sqlmodel import Session


def get_session():
    with Session(engine) as session:
        yield session