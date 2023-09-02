import socketio
import threading

server_url = "http://127.0.0.1:9000"
uuid = "fee13069-db12-49f3-bd47-405048867301"


def socket_io_client():
    cl = socketio.Client()

    @cl.on("event_name")
    def foo(data):
        print(f"client 1 {data}")

    cl.connect(f"{server_url}?uuid={uuid}")

    cl.wait()


client_thread = threading.Thread(target=socket_io_client)
client_thread.daemon = True
client_thread.start()

while True:
    pass
