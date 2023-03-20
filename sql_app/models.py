import datetime
from sqlalchemy import Column, Integer, Float, DateTime

from .database import Base

class GeoLoc(Base):
    __tablename__ = "geoLoc"

    id: int = Column(Integer, primary_key=True, index=True)
    device_id: int = Column(Integer, nullable=False)
    latitude: float = Column(Float, nullable=False)
    longitude: float = Column(Float, nullable=False)
    created_at = Column(DateTime(timezone=True), default=datetime.datetime.utcnow)
