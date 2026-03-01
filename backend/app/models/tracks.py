from sqlalchemy import Column, String, Integer
from app.db.database import Base


class Track(Base):
    __tablename__ = "tracks"
    id = Column(Integer, primary_key=True, index=True)
    spotify_id = Column(String, unique=True, nullable=False)
    name = Column(String, nullable=False)
    artists = Column(String, nullable=False)
    album = Column(String, nullable=False)
    duration_ms = Column(Integer, nullable=False)
    uri = Column(String, nullable=True)
