import threading
from socket import *

from chat_logic import LineBuffer, format_chat_message, format_join_message, format_leave_message, is_quit_command

serverPort = 12000
serverName = input("Server IP (use the server's real LAN IP, not 127.0.0.1): ").strip() or "127.0.0.1"
my_username = input("Choose a username: ").strip() or "Client"

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
clientSocket.send((my_username + "\n").encode())

# TCP has no message boundaries, so incoming bytes are read through a
# LineBuffer instead of assuming one recv() == one message.
line_buffer = LineBuffer()

peer_username = None
while peer_username is None:
    data = clientSocket.recv(1024)
    if not data:
        raise SystemExit("Server disconnected before sending its username")
    lines = line_buffer.feed(data)
    if lines:
        peer_username = lines[0] or "Server"

print(format_join_message(peer_username))


def listen_for_messages():
    while True:
        try:
            data = clientSocket.recv(1024)
        except OSError:
            break
        if not data:
            print("\n" + format_leave_message(peer_username))
            break
        for line in line_buffer.feed(data):
            print("\n" + format_chat_message(peer_username, line))


receiver = threading.Thread(target=listen_for_messages, daemon=True)
receiver.start()

print(f"Connected to {peer_username}. Type a message and press Enter. Type /quit to leave.")
while True:
    message = input()
    if is_quit_command(message):
        break
    clientSocket.send((message + "\n").encode())

clientSocket.close()
