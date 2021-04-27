from fastapi import FastAPI, WebSocket

app = FastAPI()

@app.get('/test')
async def index():
    return {'msg': 'Hello World!'}

@app.websocket('/ws')
async def ws_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        await websocket.send_text('TATA')