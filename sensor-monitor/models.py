from sqlalchemy import Column, Integer, Float, DateTime, String
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class SensorReading(Base):
    __tablename__ = "sensor_readings"
    
    id = Column(Integer, primary_key=True)
    sensor_id = Column(String, index=True)
    temperature = Column(Float)
    humidity = Column(Float)
    co2 = Column(Float)
    timestamp = Column(DateTime, default=datetime.utcnow, index=True)
