from fastapi import APIRouter, Depends
from database import db
from models import ScheduleIn
from utils.auth import require_app_key

router = APIRouter()

@router.post("/schedule", dependencies=[Depends(require_app_key)])
async def set_schedule(s: ScheduleIn):
    res = await db.schedules.insert_one(s.model_dump())
    return {"message": f"Feeding scheduled at {s.time}", "id": str(res.inserted_id)}

@router.get("/schedule", dependencies=[Depends(require_app_key)])
async def get_schedules(device_id: str = "tank-1"):
    cursor = db.schedules.find({"device_id": device_id})
    items = []
    async for d in cursor:
        d["id"] = str(d.pop("_id"))
        items.append(d)
    return items
