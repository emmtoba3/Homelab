# Sensor Monitor

FastAPI app simulating IoT sensor readings with Prometheus metrics, SQLite storage, and Grafana dashboards.

## Architecture

- **API**: FastAPI on port 8000
- **Metrics**: Prometheus on port 9090 (scrapes `/metrics`)
- **Dashboard**: Grafana on port 3000 (admin/admin)
- **Database**: SQLite

## Setup on MacBook (Development)

1. Create venv:
```bash
   cd ~/Documents/Homelab/sensor-monitor
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

API runs on http://localhost:8000

## Deploy to HP (Production)

1. Copy to server:
```bash
   scp -r ~/Documents/Homelab/homelab-repo/sensor-monitor/* homelab:~/sensor-monitor/
```

2. Build and run:
```bash
   ssh homelab "cd ~/sensor-monitor && docker compose up -d"
```

Services available at:
- API: http://192.168.100.44:8000
- Prometheus: http://192.168.100.44:9090
- Grafana: http://192.168.100.44:3000

## API Endpoints

- `GET /` — Health check
- `POST /readings/` — Create sensor reading
- `GET /readings/` — List all readings
- `GET /simulate/` — Generate and store simulated reading
- `GET /metrics` — Prometheus metrics

## Next Phase

- Automate deployment with GitHub Actions CI/CD
- Configure Grafana dashboards for sensor metrics
- Add alerting rules to Prometheus
