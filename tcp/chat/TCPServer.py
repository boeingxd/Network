import threading
from socket import *

from chat_logic import LineBuffer, format_chat_message, format_join_message, format_leave_message, is_quit_command

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print("The server is ready to receive")

my_username = input("Choose a username: ").strip() or "Server"

connectionSocket, addr = serverSocket.accept()

# TCP has no message boundaries, so every line (peer's username, then each
# chat message) is read through a LineBuffer instead of trusting recv() to
# return exactly one message per call.
line_buffer = LineBuffer()

peer_username = None
while peer_username is None:
    data = connectionSocket.recv(1024)
    if not data:
        connectionSocket.close()
        raise SystemExit("Peer disconnected before sending a username")
    lines = line_buffer.feed(data)
    if lines:
        peer_username = lines[0] or "Peer"

connectionSocket.send((my_username + "\n").encode())
print(format_join_message(peer_username))


def listen_for_messages():
    while True:
        try:
            data = connectionSocket.recv(1024)
        except OSError:
            break
        if not data:
            print("\n" + format_leave_message(peer_username))
            break
        for line in line_buffer.feed(data):
            print("\n" + format_chat_message(peer_username, line))


receiver = threading.Thread(target=listen_for_messages, daemon=True)
receiver.start()

print(f"Chatting with {peer_username}. Type a message and press Enter. Type /quit to leave.")
while True:
    message = input()
    if is_quit_command(message):
        break
    connectionSocket.send((message + "\n").encode())

connectionSocket.close()
