from fastapi import APIRouter, WebSocket
import redis

router = APIRouter()

@router.websocket('/ws')
async def info(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        await websocket.send_text(f'TATA: {data}')


