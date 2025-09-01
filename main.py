from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import sensors, feed, schedule, device

app = FastAPI(title="Fish Feeder Backend")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(sensors.router, prefix="/api", tags=["Sensors"])
app.include_router(feed.router, prefix="/api", tags=["Feeding"])
app.include_router(schedule.router, prefix="/api", tags=["Schedule"])
app.include_router(device.router, prefix="/api", tags=["Device"])

@app.get("/")
def root():
    return {"message": "Fish Feeder Backend Running 🚀"}
