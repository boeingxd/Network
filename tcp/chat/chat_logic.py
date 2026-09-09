"""Pure chat logic shared by TCPServer.py and TCPClient.py.

Kept free of socket I/O so it can be unit-tested directly.
"""

import threading


def format_chat_message(username, text):
    return f"{username}: {text}"


def format_join_message(username):
    return f"*** {username} has joined ***"


def format_leave_message(username):
    return f"*** {username} has left ***"


def is_quit_command(text):
    return text == "/quit"


class LineBuffer:
    """Reassembles newline-delimited messages from a TCP byte stream.

    TCP has no message boundaries: a single recv() can return part of a
    message, a whole message, or several messages concatenated. Feed it
    raw bytes as they arrive; it hands back only complete lines (decoded,
    without the trailing newline) and holds onto any partial tail.
    """

    def __init__(self):
        self._buffer = b""

    def feed(self, data):
        self._buffer += data
        *complete, self._buffer = self._buffer.split(b"\n")
        return [line.decode() for line in complete]


class ClientRegistry:
    """Tracks connected clients (connection -> username) for broadcast.

    Safe to share across the server's per-client threads.
    """

    def __init__(self):
        self._by_conn = {}
        self._lock = threading.Lock()

    def add(self, conn, username):
        with self._lock:
            self._by_conn[conn] = username

    def usernames(self):
        with self._lock:
            return list(self._by_conn.values())

    def remove(self, conn):
        with self._lock:
            self._by_conn.pop(conn, None)

    def others(self, conn):
        with self._lock:
            return [c for c in self._by_conn if c != conn]

    def username_for(self, conn):
        with self._lock:
            return self._by_conn.get(conn)
