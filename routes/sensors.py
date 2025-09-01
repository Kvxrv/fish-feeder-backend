from fastapi import APIRouter, Depends, Query
from typing import List, Optional
from bson import ObjectId
from database import db
from models import SensorDataIn
from utils.auth import require_app_key, require_device_key

router = APIRouter()

@router.post("/sensors", dependencies=[Depends(require_device_key)])
async def add_sensor_data(sensor: SensorDataIn):
    doc = sensor.model_dump()
    res = await db.sensors.insert_one(doc)
    return {"message": "Sensor data saved", "id": str(res.inserted_id)}

@router.get("/sensors/latest", dependencies=[Depends(require_app_key)])
async def get_latest_sensor(device_id: str = "tank-1"):
    doc = await db.sensors.find_one({"device_id": device_id}, sort=[("timestamp", -1)])
    if not doc:
        return None
    doc["id"] = str(doc.pop("_id"))
    return doc

@router.get("/sensors", dependencies=[Depends(require_app_key)])
async def list_sensors(device_id: str = "tank-1", limit: int = Query(20, ge=1, le=200), skip: int = Query(0, ge=0)):
    cursor = db.sensors.find({"device_id": device_id}).sort("timestamp", -1).skip(skip).limit(limit)
    items = []
    async for d in cursor:
        d["id"] = str(d.pop("_id"))
        items.append(d)
    return items
