import pytest
from sqlmodel import Session, delete

from database import engine, create_db_and_tables
from models import Link


@pytest.fixture(autouse=True)
def clear_database():
    create_db_and_tables()

    with Session(engine) as session:
        session.exec(delete(Link))
        session.commit()