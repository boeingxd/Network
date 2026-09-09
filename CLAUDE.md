# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repo is

DES331 (Section 2) Practical Assignment 2 — Group 8. A socket-programming exercise
covering TCP and UDP client/server communication in Python. `docs/assigment2.txt` has the
submission logistics; `docs/DES331_Assignment2.pdf` is the assignment brief;
`docs/socket_programming(self-studied).pdf` is reference material. `misc/index.html` is
leftover from Assignment 1 (HTTP server), not part of this assignment.

Files are grouped by protocol:

- `udp/UDPServer.py` / `udp/UDPClient.py` — UDP echo (uppercases the sent message, also prints
  client IP/port), unmodified — used for Section 1.
- `tcp/original/TCPServer.py` / `tcp/original/TCPClient.py` — untouched copies of the original
  uppercase-echo TCP scripts, kept for Section 2 (TCP Packet Analysis), which is separate from
  the Section 3 customization.
- `tcp/chat/TCPServer.py` / `tcp/chat/TCPClient.py` — customized for Section 3: a multi-client
  TCP group chat (threaded broadcast server, username handshake, newline-framed protocol via
  `tcp/chat/chat_logic.py`). Run tests with `cd tcp/chat && python3 -m unittest test_chat_logic`.

`tcp/original/TCPClient.py` still points at `serverName = "127.0.0.1"` — swap in a real IP
before testing across devices. `udp/UDPClient.py` and `tcp/chat/TCPClient.py` already prompt
for (or are set to) a real IP from live testing.

## Network gotcha: campus Wi-Fi blocks device-to-device traffic

The campus Wi-Fi enforces client isolation — it blocks direct device-to-device UDP/TCP traffic
between two connected devices in both directions, even though each device's own internet access
works fine. This produces a confusing "one direction works, the other doesn't" symptom that looks
like a firewall or code bug but isn't. Fix: connect all test devices to one phone's personal
mobile hotspot instead — still a real network (satisfies the no-localhost requirement), but
without the peer-isolation policy.

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
