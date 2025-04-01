from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class UserCreate(BaseModel):
    username: str
    bus_number: str
    password_hash: str  # Add this line
    route_id: str
    status: bool

class UserResponse(BaseModel):
    id: int
    username: str
    bus_number: str
    route_id: str
    status: bool

class LocationUpdate(BaseModel):
    bus_number: str
    lat: float
    lon: float

class BusLogin(BaseModel):
    bus_number: str
    password: str
class RouteDataSubmit(BaseModel):
    route_id: str
    current_lat: float
    current_lon: float
    final_lat: float
    final_lon: float
    final_destination: str
    timestamp: datetime