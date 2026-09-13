# Sensor Monitor

FastAPI app simulating IoT sensor readings with Prometheus metrics and SQLite storage.

## Setup

1. Create venv:
```bash
   python3 -m venv venv
   source venv/bin/activate
```

2. Install dependencies:
```bash
   pip install -r requirements.txt
```

3. Run locally:
```bash
   uvicorn main:app --reload
```

4. Run with Docker:
```bash
   docker-compose up --build
```

## Endpoints

- `GET /` — Health check
- `POST /readings/` — Create reading
- `GET /readings/` — List all readings
- `GET /simulate/` — Generate simulated reading
- `GET /metrics` — Prometheus metrics

## Services

- API: http://localhost:8000
- Prometheus: http://localhost:9090
- Grafana: http://localhost:3000 (admin/admin)
