import unittest

from chat_logic import (
    LineBuffer,
    format_chat_message,
    format_join_message,
    format_leave_message,
    is_quit_command,
)


class TestFormatChatMessage(unittest.TestCase):
    def test_includes_username_and_text(self):
        result = format_chat_message("Alice", "hello")
        self.assertEqual(result, "Alice: hello")


class TestFormatJoinMessage(unittest.TestCase):
    def test_announces_username_joined(self):
        result = format_join_message("Alice")
        self.assertEqual(result, "*** Alice has joined ***")


class TestFormatLeaveMessage(unittest.TestCase):
    def test_announces_username_left(self):
        result = format_leave_message("Alice")
        self.assertEqual(result, "*** Alice has left ***")


class TestIsQuitCommand(unittest.TestCase):
    def test_recognizes_slash_quit(self):
        self.assertTrue(is_quit_command("/quit"))

    def test_rejects_ordinary_message(self):
        self.assertFalse(is_quit_command("hello everyone"))


class TestLineBuffer(unittest.TestCase):
    def test_returns_nothing_until_newline_seen(self):
        buf = LineBuffer()
        self.assertEqual(buf.feed(b"partial"), [])

    def test_returns_completed_line_once_newline_arrives(self):
        buf = LineBuffer()
        buf.feed(b"hel")
        self.assertEqual(buf.feed(b"lo\n"), ["hello"])

    def test_splits_multiple_lines_coalesced_into_one_chunk(self):
        # Reproduces the coalescing bug: two sends landing in one recv().
        buf = LineBuffer()
        lines = buf.feed(b"Bob: /quit\n*** Bob has left ***\n")
        self.assertEqual(lines, ["Bob: /quit", "*** Bob has left ***"])

    def test_keeps_trailing_partial_line_for_next_feed(self):
        buf = LineBuffer()
        self.assertEqual(buf.feed(b"one\ntwo"), ["one"])
        self.assertEqual(buf.feed(b"\n"), ["two"])


if __name__ == "__main__":
    unittest.main()
