from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from . import models, schemas, crud
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/rides", response_model=list[schemas.RideOut])
def read_rides(db: Session = Depends(get_db)):
    return crud.get_rides(db)


@app.post("/rides", response_model=schemas.RideOut)
def create_ride(ride: schemas.RideCreate, db: Session = Depends(get_db)):
    return crud.create_ride(db, ride)


@app.get("/rides/{ride_id}", response_model=schemas.RideOut)
def read_ride(ride_id: int, db: Session = Depends(get_db)):
    db_ride = crud.get_ride(db, ride_id)
    if not db_ride:
        raise HTTPException(status_code=404, detail="Ride not found")
    return db_ride


@app.put("/rides/{ride_id}", response_model=schemas.RideOut)
def update_ride(ride_id: int, ride: schemas.RideUpdate, db: Session = Depends(get_db)):
    db_ride = crud.update_ride(db, ride_id, ride)
    if not db_ride:
        raise HTTPException(status_code=404, detail="Ride not found")
    return db_ride


@app.delete("/rides/{ride_id}")
def delete_ride(ride_id: int, db: Session = Depends(get_db)):
    db_ride = crud.delete_ride(db, ride_id)
    if not db_ride:
        raise HTTPException(status_code=404, detail="Ride not found")
    return {"message": "Ride deleted"}