---
name: check-submission
description: Verify the three required Assignment 2 submission items (PDF report, Wireshark capture, customized TCP/UDP source) are present and consistent before submitting. Use when the user asks to check, verify, or prepare the assignment submission.
---

Check this repo against the Assignment 2 submission requirements (see CLAUDE.md /
`assigment2.txt` for the full brief) and report a clear pass/fail per item:

1. **PDF report** — Is there a PDF report (distinct from the assignment brief / reference
   material PDFs) containing answers, explanations, diagrams, and required screenshots?
   Look for it in the repo; if none exists, say so plainly rather than guessing.

2. **Wireshark capture** — Is there a `.pcap`/`.pcapng` file in the repo? If found, note its
   name/location. Flag if none is present — this is required and easy to forget to commit.

3. **Customized source code** — Identify which protocol (TCP or UDP) was customized for
   Section 3 ("Designing Your Own Network Application"). Compare the current
   `TCPServer.py`/`TCPClient.py` or `UDPServer.py`/`UDPClient.py` against the original
   echo-server versions (uppercase-the-sentence) to confirm they've actually been modified,
   not left as the base example. If the client was also modified, confirm it's included too.

4. **Localhost check** — Grep the customized client/server for `127.0.0.1` or `localhost`.
   Flag this loudly: the assignment requires real device-to-device communication, and
   localhost-only code will not satisfy the requirement even if everything else is correct.

5. **Consistency** — Do the report's description of the protocol/behavior, the capture file,
   and the submitted source code all agree with each other (same protocol, same behavior)?

Summarize as a short checklist (✅/❌ per item) with specific file names, not generic advice.
Do not modify any files as part of this check — it's a read-only verification pass.
