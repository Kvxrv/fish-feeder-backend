import os
from fastapi import Header, HTTPException, status

APP_API_KEY = os.getenv("APP_API_KEY", "dev-app-key")
DEVICE_API_KEY = os.getenv("DEVICE_API_KEY", "dev-device-key")

async def require_app_key(x_api_key: str = Header(None)):
    if x_api_key != APP_API_KEY:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid app API key")

async def require_device_key(x_device_key: str = Header(None)):
    if x_device_key != DEVICE_API_KEY:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid device key")
