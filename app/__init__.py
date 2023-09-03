import socketio
from fastapi import FastAPI
from app.utils import get_info_raspbarrypi
import RPi.GPIO as GPIO

app = FastAPI()

server_url = "http://127.0.0.1:9000"

uuid = "fee13069-db12-49f3-bd47-405048867301"

sio = socketio.AsyncClient()


led_pin = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(led_pin, GPIO.OUT)


def open_door():
    GPIO.output(led_pin, GPIO.HIGH)


def close_door():
    GPIO.output(led_pin, GPIO.LOW)


@app.on_event("startup")
async def startup_event():
    await sio.connect(f"{server_url}?uuid={uuid}")
    print("🔌 Connected")


@app.get("/send_message")
async def send_message(message):
    await sio.emit("receive_message", "Olá, servidor principal!")
    return {"message": "Dados enviados com sucesso"}


@sio.on("receive_message")
async def receive_message(message):
    try:
        if message == "get_info_raspbarrypi":
            info = get_info_raspbarrypi()
            await sio.emit("receive_message", info)
        elif message == "open_the_door":
            print("Open door")
            message = "Open door"
            await sio.emit("receive_message", message)
    except Exception as e:
        print(f"Error: {e}")
