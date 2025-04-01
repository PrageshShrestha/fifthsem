# models.py
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float, DateTime, JSON
from sqlalchemy.orm import relationship
from datetime import datetime
from base import Base  # Import Base from base.py

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    bus_number = Column(String, unique=True, index=True)
    route_id = Column(String)
    password_hash = Column(String)
    status = Column(Boolean, default=True)
    
    bus_info = relationship("BusLocation", back_populates="bus", uselist=False)
    def verify_password(self, password):
        
        return self.password_hash == password
class BusLocation(Base):
    __tablename__ = "bus_locations"
    
    id = Column(Integer, primary_key=True, index=True)
    bus_number = Column(String, ForeignKey("users.bus_number"), unique=True, nullable=False)
    current_lat = Column(Float, nullable=False)
    current_lon = Column(Float, nullable=False)
    last_5_sec_locations = Column(JSON, default=[])
    last_15_sec_location = Column(JSON, nullable=True)
    last_25_sec_location = Column(JSON, nullable=True)
    last_updated = Column(DateTime, default=datetime.utcnow)
    
    bus = relationship("User", back_populates="bus_info")

class RouteInfo(Base):
    __tablename__ = "route_info"
    
    id = Column(Integer, primary_key=True, index=True)
    route_id = Column(String, unique=True, nullable=False)
    route_name = Column(String, nullable=False)
    coordinates = Column(JSON, default=[])
    
    def add_coordinates(self, new_coords):
        self.coordinates.extend(new_coords)
        
        
        
        
        

