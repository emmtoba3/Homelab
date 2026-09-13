from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from prometheus_fastapi_instrumentator import Instrumentator
from database import SessionLocal, get_db, engine
from models import Base, SensorReading as SensorReadingModel
from schemas import SensorReadingCreate, SensorReading
from simulator import generate_sensor_data

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Sensor Monitor API", version="1.0.0")

Instrumentator().instrument(app).expose(app)

@app.get("/")
def read_root():
    return {"status": "healthy", "service": "Sensor Monitor"}

@app.post("/readings/", response_model=SensorReading)
def create_reading(reading: SensorReadingCreate, db: Session = Depends(get_db)):
    db_reading = SensorReadingModel(**reading.dict())
    db.add(db_reading)
    db.commit()
    db.refresh(db_reading)
    return db_reading

@app.get("/readings/", response_model=list[SensorReading])
def list_readings(db: Session = Depends(get_db)):
    return db.query(SensorReadingModel).all()

@app.get("/simulate/")
def simulate_reading(db: Session = Depends(get_db)):
    data = generate_sensor_data()
    reading = SensorReadingCreate(**data)
    return create_reading(reading, db)
