from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse
from sse_starlette.sse import EventSourceResponse
import asyncio
from datetime import datetime


app = FastAPI()

class ConnectionManager:
    def __init__(self):
        self.active_connections: list[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def broadcast(self, message: str):
        for connection in self.active_connections:
            await connection.send_text(message)


manager = ConnectionManager()



@app.websocket("/ws")
async def websocket_echo(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            data = await websocket.receive_text()
            await websocket.send_text(f"Echo: {data}")
    except WebSocketDisconnect:
        print("Client disconnected")



@app.websocket("/ws/chat")
async def websocket_chat(websocket: WebSocket):
    await manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            await manager.broadcast(f"Message: {data}")
    except WebSocketDisconnect:
        manager.disconnect(websocket)
        await manager.broadcast("A user left the chat.")


@app.get("/events/clock")
async def sse_clock():
    async def generate():
        while True:
            now = datetime.now().strftime("%H:%M:%S")
            yield {"data": f"Time: {now}"}
            await asyncio.sleep(1)
    return EventSourceResponse(generate())



@app.get("/events/counter")
async def sse_counter():
    async def generate():
        count = 0
        while True:
            yield {"data": f"Count: {count}"}
            count += 1
            await asyncio.sleep(1)
    return EventSourceResponse(generate())


@app.get("/")
async def get():
    with open("index.html", encoding="utf-8") as f:
        return HTMLResponse(f.read())