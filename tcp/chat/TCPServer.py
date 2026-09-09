import threading
from socket import *

from chat_logic import (
    ClientRegistry,
    LineBuffer,
    format_chat_message,
    format_join_message,
    format_leave_message,
)

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(5)
print("The server is ready to receive")

clients = ClientRegistry()


def broadcast(text, sender_conn):
    payload = (text + "\n").encode()
    for conn in clients.others(sender_conn):
        try:
            conn.send(payload)
        except OSError:
            pass  # that client's own handler thread will clean it up


def handle_client(connectionSocket, addr):
    # TCP has no message boundaries, so every line (username, then each chat
    # message) is read through a LineBuffer instead of trusting recv() to
    # return exactly one message per call.
    line_buffer = LineBuffer()

    username = None
    while username is None:
        data = connectionSocket.recv(1024)
        if not data:
            connectionSocket.close()
            return
        lines = line_buffer.feed(data)
        if lines:
            username = lines[0] or "Anonymous"

    clients.add(connectionSocket, username)
    print(f"{username} connected from {addr}")
    broadcast(format_join_message(username), connectionSocket)

    try:
        while True:
            data = connectionSocket.recv(1024)
            if not data:
                break
            for text in line_buffer.feed(data):
                broadcast(format_chat_message(username, text), connectionSocket)
    finally:
        clients.remove(connectionSocket)
        broadcast(format_leave_message(username), connectionSocket)
        connectionSocket.close()
        print(f"{username} disconnected")


while True:
    connectionSocket, addr = serverSocket.accept()
    threading.Thread(target=handle_client, args=(connectionSocket, addr), daemon=True).start()
