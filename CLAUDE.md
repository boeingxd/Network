# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repo is

DES331 (Section 2) Practical Assignment 2 — Group 8. A socket-programming exercise
covering TCP and UDP client/server communication in Python. `assigment2.txt` has the
assignment brief; `DES331_Assignment2.pdf` and `socket_programming(self-studied).pdf` are
reference material. `misc/index.html` is leftover from Assignment 1 (HTTP server), not part
of this assignment.

- `TCPServer.py` / `TCPClient.py` — TCP echo (uppercases the sent sentence).
- `UDPServer.py` / `UDPClient.py` — UDP echo (uppercases the sent message, also prints client IP/port).

Both pairs currently point at `serverName = "127.0.0.1"` for local testing.

## Critical constraint: localhost is not acceptable for submission

The assignment explicitly requires **actual communication between separate devices over a
network** — running only on localhost is NOT accepted and will not satisfy the requirement.
Before final testing/capture, `serverName`/`serverPort` in the client scripts need to point
at the real IP of the machine running the server (not `127.0.0.1`), and the Wireshark capture
must show that real device-to-device traffic.

## Submission requirements (per assigment2.txt)

One combined group submission (Group Leader or Assistant Leader submits), consisting of:
1. One PDF report — all answers, explanations, diagrams, required screenshots.
2. One Wireshark capture file (`.pcap`/`.pcapng`) of the TCP/UDP communication demonstrated.
3. Customized server Python source for Section 3 ("Designing Your Own Network Application")
   — TCP *or* UDP, not both required. If the client was also modified, submit that too.

These three must stay consistent with each other (same protocol, same behavior described in
the report). Missing the customized source = zero marks for Section 3. Deadline: 23 Sep 2026.

## Git workflow

This repo is shared with groupmates over git — others push/pull directly, not just through
this session. Keep commits scoped to what was actually asked, use clear commit messages, and
don't force-push or rewrite shared history without asking first.
