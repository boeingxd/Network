---
name: check-submission
description: Verify the three required Assignment 2 submission items (PDF report, Wireshark capture, customized TCP/UDP source) are present and consistent before submitting. Use when the user asks to check, verify, or prepare the assignment submission.
---

Check this repo against the Assignment 2 submission requirements (see CLAUDE.md /
`docs/assigment2.txt` for the full brief) and report a clear pass/fail per item:

1. **PDF report** — Is there a PDF report (distinct from `docs/DES331_Assignment2.pdf` and
   `docs/socket_programming(self-studied).pdf`, which are brief/reference material, not the
   report) containing answers, explanations, diagrams, and required screenshots? Look for it
   in the repo; if none exists, say so plainly rather than guessing.

2. **Wireshark capture** — Is there a `.pcap`/`.pcapng` file in the repo? If found, note its
   name/location. Flag if none is present — this is required and easy to forget to commit.

3. **Customized source code** — Section 3 is customized in `tcp/chat/` (`TCPServer.py`,
   `TCPClient.py`, `chat_logic.py`) — a 1-to-1 TCP peer chat, not the original letter-case
   transform. Confirm those files are actually present and still reflect that customization
   (not reverted to the echo behavior in `tcp/original/` or `udp/`). If the client was also
   modified, confirm it's included too.

4. **Localhost check** — Grep the customized client/server for `127.0.0.1` or `localhost`.
   Flag this loudly: the assignment requires real device-to-device communication, and
   localhost-only code will not satisfy the requirement even if everything else is correct.

5. **Consistency** — Do the report's description of the protocol/behavior, the capture file,
   and the submitted source code all agree with each other (same protocol, same behavior)?

Summarize as a short checklist (✅/❌ per item) with specific file names, not generic advice.
Do not modify any files as part of this check — it's a read-only verification pass.
