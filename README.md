# EIMS Pro — Enterprise Infrastructure Monitoring System

A professional Python/Flask infrastructure monitoring dashboard designed as a portfolio and learning project.

## Features
- Live CPU, memory, disk and process telemetry
- Threshold-based alert engine
- Server inventory with SQLite
- CSV and PDF reports
- REST API at `/api/metrics`
- Responsive enterprise dark UI
- Modular Python architecture

## Run
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
python app.py
```
Open `http://127.0.0.1:5000`.

## Architecture
Browser → Flask routes → monitoring engine → psutil / SQLite → reports

## Important scope
The first version monitors the machine running Flask. A production-grade next phase can add secure remote agents, authentication/RBAC, PostgreSQL, WebSockets, background workers, audit logging, Docker and CI/CD.
