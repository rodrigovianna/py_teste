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
