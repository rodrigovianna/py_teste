from typing import List

from sqlalchemy.orm import Session

from sql_app.models import GeoLoc

class GeoLocRepository:
    @staticmethod
    def save(db: Session, geoLoc: GeoLoc) -> List[GeoLoc]:
        if geoLoc.id:
            db.merge(geoLoc)
        else:
            db.add(geoLoc)
        db.commit()
        return geoLoc

    @staticmethod
    def find_all(db: Session) -> List[GeoLoc]:
        return db.query(GeoLoc).all()

    @staticmethod
    def find_by_device_id(db: Session, id: int) -> GeoLoc:
        return db.query(GeoLoc).filter(GeoLoc.device_id == id).all()
