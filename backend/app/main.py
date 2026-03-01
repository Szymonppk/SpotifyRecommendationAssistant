from fastapi import FastAPI
from app.db.database import Base, engine
from app.models import users, tracks

app = FastAPI()
Base.metadata.create_all(bind=engine)
