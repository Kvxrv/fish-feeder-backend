# Fish Feeder Backend (FastAPI + MongoDB)

## Quick Start
1) Create `.env` from `.env.example` and fill secrets.
2) Install deps: `pip install -r requirements.txt`
3) Run: `uvicorn main:app --reload --port 8000`
4) Open docs at: `http://localhost:8000/docs`

## Endpoints (short)
- POST `/api/sensors` (device) — send sensor data
- GET  `/api/sensors/latest` (app) — latest reading
- GET  `/api/sensors` (app) — paginated readings
- POST `/api/feed` (app) — enqueue feed command
- GET  `/api/feeding-history` (app) — last 50 feed logs
- GET  `/api/device/{id}/pull` (device) — pull commands
- POST `/api/device/{id}/ack` (device) — ack a command
- POST `/api/schedule` (app) — create a schedule (HH:MM)
- GET  `/api/schedule` (app) — list schedules

## Auth
- Flutter app calls include header: `x-api-key: <APP_API_KEY>`
- ESP32 calls include header: `x-device-key: <DEVICE_API_KEY>`

## Deploy to Render
- Push this folder to GitHub.
- Create **Web Service** on Render → connect repo.
- Set environment variables `MONGO_URI`, `APP_API_KEY`, `DEVICE_API_KEY`.
- Render uses `render.yaml` to start the service.
