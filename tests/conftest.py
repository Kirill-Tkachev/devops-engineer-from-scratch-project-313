import os

os.environ["TESTING"] = "1"

import pytest
from sqlmodel import Session, delete

from app.database import engine, create_db_and_tables
from app.models import Link


@pytest.fixture(autouse=True)
def clear_database():
    create_db_and_tables()

    with Session(engine) as session:
        session.exec(delete(Link))
        session.commit()