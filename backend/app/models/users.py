from sqlalchemy import Column, String, Integer
from app.db.database import Base


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, nullable=False, index=True)
    email = Column(String, unique=True, nullable=False, index=True)
    passwoord = Column(String,nullable=False)
    spotify_id = Column(String,unique=True,nullable=False)
    