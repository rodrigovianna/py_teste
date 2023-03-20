from typing import List
from datetime import datetime
from pydantic import BaseModel

class GeoLocBase(BaseModel):
    device_id: int
    latitude: float
    longitude: float

class GeoLocRequest(GeoLocBase):
    ...

class GeoLocList(GeoLocBase):
    List[GeoLocRequest]

class GeoLocResponse(GeoLocBase):
    id: int
    created_at: datetime
    class Config:
        orm_mode = True
