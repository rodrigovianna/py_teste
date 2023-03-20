from typing import List

from fastapi import FastAPI, Depends, HTTPException, status, Request, Response
from sqlalchemy.orm import Session

from sql_app.models import GeoLoc
from sql_app.database import engine, Base, get_db
from repositories import GeoLocRepository
from sql_app.schemas import GeoLocResponse, GeoLocList

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def home():
    return {"return": "Live"}

@app.post("/geolocs",status_code=status.HTTP_201_CREATED)
def create(request: List[GeoLocList], db: Session = Depends(get_db)):
    geoLoc = []
    for geoloc in request :
        r = GeoLocRepository.save(db, GeoLoc(**geoloc.dict()))
        geoLoc.append(GeoLocResponse.from_orm(r))
    return geoLoc

@app.get("/geolocs", response_model=List[GeoLocResponse])
def find_all(db: Session = Depends(get_db)):
    geoLocs = GeoLocRepository.find_all(db)
    return [GeoLocResponse.from_orm(geoLoc) for geoLoc in geoLocs]

@app.get("/geolocs/{device_id}", response_model=List[GeoLocResponse])
def find_by_device_id(device_id: int, db: Session = Depends(get_db)):
    geoLocs = GeoLocRepository.find_by_device_id(db, device_id)
    if not geoLocs:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Device não encontrado"
        )
    return [GeoLocResponse.from_orm(geoLoc) for geoLoc in geoLocs]
