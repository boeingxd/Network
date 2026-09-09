"""Pure chat logic shared by TCPServer.py and TCPClient.py.

Kept free of socket I/O so it can be unit-tested directly.
"""

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
