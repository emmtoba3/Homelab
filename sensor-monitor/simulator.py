import random
from datetime import datetime

def generate_sensor_data():
    return {
        "sensor_id": f"sensor_{random.randint(1, 5)}",
        "temperature": round(20 + random.uniform(-5, 5), 2),
        "humidity": round(40 + random.uniform(-10, 10), 2),
        "co2": round(400 + random.uniform(-50, 50), 2),
    }
