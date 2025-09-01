from fastapi import APIRouter, Depends
from datetime import datetime
from database import db
from models import FeedLog
from utils.auth import require_app_key

router = APIRouter()

@router.post("/feed", dependencies=[Depends(require_app_key)])
async def feed_fish(log: FeedLog):
    # 1) Save feed log
    await db.feeding.insert_one(log.model_dump())

    # 2) Enqueue command for device to execute
    cmd = {
        "device_id": log.device_id,
        "type": "feed",
        "payload": {"seconds": 2},
        "status": "pending",
        "created_at": datetime.utcnow(),
    }
    res = await db.commands.insert_one(cmd)
    return {"message": "Feeding queued", "command_id": str(res.inserted_id)}

@router.get("/feeding-history", dependencies=[Depends(require_app_key)])
async def get_feeding_history(device_id: str = "tank-1", limit: int = 50):
    cursor = db.feeding.find({"device_id": device_id}).sort("time", -1).limit(limit)
    items = []
    async for d in cursor:
        d["id"] = str(d.pop("_id"))
        items.append(d)
    return items
