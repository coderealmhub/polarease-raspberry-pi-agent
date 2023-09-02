import socketio
from fastapi import FastAPI

app = FastAPI()

server_url = "http://127.0.0.1:9000"

uuid = "fee13069-db12-49f3-bd47-405048867301"

sio = socketio.AsyncClient()


@app.on_event("startup")
async def startup_event():
    await sio.connect(f"{server_url}?uuid={uuid}")
    print("🔌 Connected")


@app.get("/send_message")
async def send_message():
    await sio.emit("receive", "Olá, servidor principal!")

    return {"message": "Dados enviados com sucesso"}


@sio.on("receive")
async def receive(message):
    try:
        print(f"message: {message}")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
