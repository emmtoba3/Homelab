from pydantic import BaseModel
from datetime import datetime

class SensorReadingCreate(BaseModel):
    sensor_id: str
    temperature: float
    humidity: float
    co2: float

class SensorReading(SensorReadingCreate):
    id: int
    timestamp: datetime
    
    class Config:
        from_attributes = True
