# Section 3: Designing Your Own Network Application — Draft Answers

Draft answers for the report, based on `tcp/chat/` (`TCPServer.py`, `TCPClient.py`,
`chat_logic.py`). Copy/adapt the wording below into the PDF report. Q4 and Q5 need an actual
Wireshark screenshot from a live capture — see the note at the bottom for exactly how to get
them; everything else here is ready to use.

---

## 1. Briefly describe your idea for customizing the provided source code. (10 points)

We replaced the original letter-case transformation service with a **real-time, two-way text
chat application** between one server and one client ("peer chat"). Instead of the server
performing a single fixed transformation on one message and then closing the connection, our
version keeps the TCP connection open for an ongoing conversation: each side identifies itself
with a username when the connection is established, and either side can send and receive text
messages freely until one of them ends the chat.

## 2. Describe the requirements of your network application, including its input, output, and application logic. (10 points)

**Input:** each side's typed text — first a chosen username, then any number of chat messages
typed at the keyboard over the lifetime of the connection.

**Output:** messages received from the other side are printed to the terminal prefixed with the
sender's username (e.g. `Alice: hello`), along with join/leave notifications
(`*** Alice has joined ***`) when the connection opens or closes.

**Application logic:**
- **Handshake:** on connect, the client sends its username as the first line of the stream; the
  server reads it, then sends its own username back — a two-way handshake so each side knows
  who it's talking to before any chat message is exchanged.
- **Concurrent send/receive:** both sides run a background thread that continuously listens for
  incoming data and prints it, while the main thread reads the user's typed input and sends it —
  so messages can be received at any moment, not in strict request/response lock-step.
- **Message framing:** TCP is a byte stream with no built-in message boundaries, so every line
  sent (username, then each chat message) is terminated with `\n` on the sender side and
  reassembled by a small buffering layer (`LineBuffer` in `chat_logic.py`) on the receiver side.
  This guarantees multiple quick messages — or a message split across two `recv()` calls — are
  still correctly reconstructed into individual lines.
- **Exit:** typing `/quit` on either side closes that side's socket and ends the chat cleanly.

## 3. Based on your answer to Question 3.2, which transport-layer protocol (TCP or UDP) is more suitable for your network application? Clearly explain your reasoning. (10 points)

**TCP** is the right choice, for three reasons:

1. **Reliable, in-order delivery matters for a conversation.** If messages could be dropped or
   arrive out of order, a chat becomes confusing or nonsensical — e.g. a reply appearing before
   the message it's replying to. UDP gives no such guarantee; TCP does.
2. **Connection-oriented semantics match the application model.** A chat is inherently an
   ongoing, stateful conversation between two identified parties, not a series of independent,
   stateless requests — which is exactly what TCP's connection model represents, and what UDP
   (a fire-and-forget datagram protocol) does not.
3. **This was confirmed directly during development, not just in theory.** While building the
   app, a real bug surfaced: because TCP delivers one continuous byte stream, two messages sent
   back-to-back briefly arrived concatenated in a single `recv()` call on the receiving side, with
   no boundary between them. The fix was to add explicit newline framing (`LineBuffer`) — but the
   key point is what TCP guaranteed us *despite* that bug: every byte we sent arrived, in the
   exact order we sent it; we only had to solve *where one message ends and the next begins*, not
   worry about a message vanishing or being reordered. UDP would add an additional failure mode
   on top of that (datagrams silently dropped or delivered out of order), which is strictly worse
   for a text conversation where every word matters. UDP's lower latency/overhead is a better
   trade-off for loss-tolerant, high-volume traffic (e.g. live video/audio, sensor telemetry) —
   not for this application.

## 4. Capture a screenshot showing the packet where the client sends a message to the server. (1 point)

*(See "Getting the Q4/Q5 screenshots" below — requires a live capture with your groupmate.)*

## 5. Capture a screenshot showing the packet where the server replies to the client. (1 point)

*(See "Getting the Q4/Q5 screenshots" below — requires a live capture with your groupmate.)*

## 6. Describe a real-world scenario in which your network application could be applied. Explain how your application could improve the service in that scenario. (8 points)

A real-world fit is a **lightweight internal help-desk / IT support line**: instead of routing a
request through email or an asynchronous ticket system, a user in need of support connects
directly to a specific technician's machine for a live, real-time back-and-forth conversation.

This improves the scenario in two concrete ways:
- **Immediacy** — replacing the round-trip delay of email/tickets with instant, synchronous
  back-and-forth, which matters when troubleshooting something time-sensitive (e.g. a system
  outage).
- **Reliability of the conversation itself** — TCP's guaranteed, in-order delivery means no
  critical troubleshooting instruction (e.g. "run this command now") is ever silently lost or
  reordered, which would be far more damaging in a support context than in casual chat.

The same design also fits any low-connectivity local-network scenario where two specific devices
need a direct, dependable text channel without relying on external internet infrastructure — e.g.
a technician's laptop issuing commands to a piece of lab/field equipment over a local link.

---

## Getting the Q4/Q5 screenshots

These two need a real packet capture, not just text — walk through this with your groupmate:

1. Both connect to the same personal mobile hotspot (campus Wi-Fi blocks device-to-device
   traffic — see the "Network gotcha" note in `CLAUDE.md`).
2. Start a Wireshark capture on that Wi-Fi interface.
3. Run `cd tcp/chat && python3 TCPServer.py` on one machine, `python3 TCPClient.py` on the
   other (pointing at the server's real IP). Exchange one message each way.
4. Filter the capture: `tcp.port == 12000` (or `llc` / `tcp || llc` if it shows as LLC — a known
   macOS Wi-Fi capture quirk, harmless).
5. Screenshot the `PSH, ACK` segment client → server (payload = the client's typed message) for
   Q4, and the `PSH, ACK` segment server → client (payload = the server's typed reply) for Q5.

Full step-by-step is in the conversation history with Claude; ask if you need it repeated.
