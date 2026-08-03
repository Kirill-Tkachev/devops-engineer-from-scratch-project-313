from fastapi import FastAPI, HTTPException, Depends
from database import create_db_and_tables, get_session
from sqlmodel import Session, select
from models import Link
from schemas import LinkCreate, LinkUpdate
from sqlalchemy.exc import IntegrityError
from utils import build_short_url

app = FastAPI()


@app.on_event("startup")
def on_startup():
    create_db_and_tables()


@app.get("/ping")
def ping():
    return "pong"


@app.post("/api/links", status_code=201)
def create_link(
    link: LinkCreate,
    session: Session = Depends(get_session),
):
    db_link = Link(
        original_url=link.original_url,
        short_name=link.short_name,
    )

    session.add(db_link)

    try:
        session.commit()
    except IntegrityError:
        session.rollback()
        raise HTTPException(
            status_code=409,
            detail="Short name already exists",
        )

    session.refresh(db_link)

    return {
    "id": db_link.id,
    "original_url": db_link.original_url,
    "short_name": db_link.short_name,
    "short_url": build_short_url(db_link.short_name),
    }


@app.get("/api/links")
def get_links(session: Session = Depends(get_session)):
    links = session.exec(select(Link)).all()

    return [
        {
        "id": link.id,
        "original_url": link.original_url,
        "short_name": link.short_name,
        "short_url": build_short_url(link.short_name),
        }
        for link in links
    ]


@app.get("/api/links/{id}")
def get_link(
    id: int,
    session: Session = Depends(get_session),
):
    link = session.get(Link, id)

    if link is None:
        raise HTTPException(status_code=404, detail="Link not found")

    return {
    "id": link.id,
    "original_url": link.original_url,
    "short_name": link.short_name,
    "short_url": build_short_url(link.short_name),
    }


@app.put("/api/links/{id}")
def update_link(
    id: int,
    link_data: LinkUpdate,
    session: Session = Depends(get_session),
):
    link = session.get(Link, id)

    if link is None:
        raise HTTPException(status_code=404, detail="Link not found")

    link.original_url = link_data.original_url
    link.short_name = link_data.short_name

    session.add(link)
    session.commit()
    session.refresh(link)

    return {
    "id": link.id,
    "original_url": link.original_url,
    "short_name": link.short_name,
    "short_url": build_short_url(link.short_name),
    }


@app.delete("/api/links/{id}", status_code=204)
def delete_link(
    id: int,
    session: Session = Depends(get_session),
):
    link = session.get(Link, id)

    if link is None:
        raise HTTPException(status_code=404, detail="Link not found")

    session.delete(link)
    session.commit()