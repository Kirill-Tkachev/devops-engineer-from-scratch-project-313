from fastapi import FastAPI
from app.database import create_db_and_tables
from fastapi.middleware.cors import CORSMiddleware
from app.routes import register_routes

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
def on_startup():
    create_db_and_tables()


register_routes(app)