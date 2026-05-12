from pydantic import BaseModel, Field
from datetime import datetime


class RideBase(BaseModel):
    passenger_name: str
    driver_name: str
    origin: str
    destination: str
    price: float = Field(ge=0)
    status: str


class RideCreate(RideBase):
    pass


class RideUpdate(RideBase):
    pass


class RideOut(RideBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True