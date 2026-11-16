
from fastapi import FastAPI
from sqlalchemy import text

from app.database import engine, Base
from app import models
from app.routes import auth, projects, tasks

app = FastAPI(title="TeamSpace API")
app.include_router(auth.router)
app.include_router(projects.router)
app.include_router(tasks.router)

@app.on_event("startup")
def create_tables():
    
    Base.metadata.create_all(bind=engine)


@app.get("/")
def home():
    return {"message": "Welcome to TeamSpace API"}


@app.get("/db-test")
def test_database():
    try:
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))

        return {"message": "Database connected successfully!"}

    except Exception as e:
        return {"error": str(e)}
