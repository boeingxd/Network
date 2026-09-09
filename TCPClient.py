import threading
from socket import *

from chat_logic import LineBuffer, is_quit_command

serverPort = 12000
serverName = input("Server IP (use the server's real LAN IP, not 127.0.0.1): ").strip() or "127.0.0.1"
username = input("Choose a username: ").strip() or "Anonymous"

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
clientSocket.send((username + "\n").encode())


def listen_for_messages():
    # TCP has no message boundaries, so incoming bytes are read through a
    # LineBuffer instead of assuming one recv() == one message.
    line_buffer = LineBuffer()
    while True:
        try:
            data = clientSocket.recv(1024)
        except OSError:
            break
        if not data:
            print("\nDisconnected from server.")
            break
        for line in line_buffer.feed(data):
            print("\n" + line)


receiver = threading.Thread(target=listen_for_messages, daemon=True)
receiver.start()

print("Connected. Type a message and press Enter. Type /quit to leave.")
while True:
    message = input()
    if is_quit_command(message):
        break
    clientSocket.send((message + "\n").encode())

clientSocket.close()
