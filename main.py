from fastapi import FastAPI, Request
from loguru import logger
from datetime import datetime


app = FastAPI()


@app.get("/{serial}")
def mock_get(request: Request, serial: int):
    _msg = f"GET request with #{serial}# received from {request.client} at {datetime.now().isoformat()}"
    logger.info(_msg)
    return {
        "success": True,
        "msg": _msg,
        "data": []
    }
