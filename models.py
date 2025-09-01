from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional, List

class SensorDataIn(BaseModel):
    device_id: str = "tank-1"
    temperature: float
    ph: float
    salinity: float
    timestamp: datetime = Field(default_factory=datetime.utcnow)

class SensorDataOut(SensorDataIn):
    id: str

class FeedLog(BaseModel):
    device_id: str = "tank-1"
    mode: str  # "manual" | "scheduled"
    time: datetime = Field(default_factory=datetime.utcnow)

class ScheduleIn(BaseModel):
    device_id: str = "tank-1"
    time: str  # "HH:MM" 24h

class ScheduleOut(ScheduleIn):
    id: str

class Command(BaseModel):
    id: str
    device_id: str
    type: str  # "feed"
    payload: dict = {}
    status: str  # "pending" | "sent" | "ack"
    created_at: datetime
