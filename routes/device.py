from fastapi import APIRouter, Depends
from bson import ObjectId
from database import db
from utils.auth import require_device_key

router = APIRouter()

@router.get("/device/{device_id}/pull", dependencies=[Depends(require_device_key)])
async def pull_commands(device_id: str):
    # Find one pending command and mark as 'sent'
    doc = await db.commands.find_one_and_update(
        {"device_id": device_id, "status": "pending"},
        {"$set": {"status": "sent"}},
        sort=[("created_at", 1)],
        return_document=True,
    )
    if not doc:
        return {"commands": []}
    doc["id"] = str(doc.pop("_id"))
    return {"commands": [doc]}

@router.post("/device/{device_id}/ack", dependencies=[Depends(require_device_key)])
async def ack_command(device_id: str, command_id: str):
    await db.commands.update_one(
        {"_id": ObjectId(command_id), "device_id": device_id},
        {"$set": {"status": "ack"}}
    )
    return {"message": "acknowledged"}
