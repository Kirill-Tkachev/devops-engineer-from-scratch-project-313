import pytest
from sqlmodel import Session, delete

from database import engine
from models import Link


@pytest.fixture(autouse=True)
def clear_database():
    with Session(engine) as session:
        session.exec(delete(Link))
        session.commit()