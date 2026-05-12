from sqlalchemy.orm import Session
from . import models, schemas


def get_rides(db: Session):
    return db.query(models.Ride).all()


def get_ride(db: Session, ride_id: int):
    return db.query(models.Ride).filter(models.Ride.id == ride_id).first()


def create_ride(db: Session, ride: schemas.RideCreate):
    db_ride = models.Ride(**ride.dict())
    db.add(db_ride)
    db.commit()
    db.refresh(db_ride)
    return db_ride


def update_ride(db: Session, ride_id: int, ride: schemas.RideUpdate):
    db_ride = get_ride(db, ride_id)
    if not db_ride:
        return None

    for key, value in ride.dict().items():
        setattr(db_ride, key, value)

    db.commit()
    db.refresh(db_ride)
    return db_ride


def delete_ride(db: Session, ride_id: int):
    db_ride = get_ride(db, ride_id)
    if not db_ride:
        return None

    db.delete(db_ride)
    db.commit()
    return db_ride