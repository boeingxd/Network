# Assignment 2: Socket Programming — Summary for Group Members

**Course:** DES331 Computer Network Architecture and Protocols, Semester 1/2026, SIIT Thammasat

## TL;DR

This is a group assignment about socket programming with Python. You'll run the provided TCP and UDP server/client code (which originally just converts lowercase letters to uppercase), use Wireshark to capture and analyze the packets exchanged between them, and then design and build your own custom network application by modifying the server-side logic — choosing whichever transport protocol (TCP or UDP) best fits your application and justifying that choice. The whole thing must be done using a real network set up between actual devices in your group, not a single computer talking to itself.

> **CRITICAL CONSTRAINT: You MUST use a real network between actual physical devices.**
> **Running the assignment on `localhost` only is NOT acceptable and will result in ZERO marks.** This applies to the whole assignment.

## Section-by-Section Breakdown

### Warm-up Section (10 points)
- **Group photo (5 pts):** Show all team members participating. Each member must be clearly identified **in the photo** with name, student ID, and the date the assignment was done. (Purpose: verifies everyone participated.)
- **Network topology diagram (5 pts):** Briefly draw your group's network topology. Must clearly show how the TCP/UDP server and client devices are connected. **IP address of each device is required.**

### Section 1: UDP Packet Analysis (10 points)
Run the provided `UDPServer.py` and `UDPClient.py`, capture traffic with Wireshark, and answer:
1. **(1 pt)** Wireshark screenshots showing UDP request and response packets (hint: filter `udp` or `llc`).
2. **(3 pts)** Identify the socket addresses of both the UDP server and client.
3. **(1 pt)** Screenshot of the packet where the client sends a message to the server.
4. **(1 pt)** Screenshot of the packet where the server replies to the client.
5. **(4 pts)** Diagram of the socket communication between client and server — must include communication direction, port numbers, and IP addresses (Application + Transport layer only; see Lecture 4, connectionless part).

### Section 2: TCP Packet Analysis (20 points)
Run your revised `TCPServer.py` and `TCPClient.py`, capture traffic with Wireshark, and answer:
1. **(1 pt)** Wireshark screenshots showing TCP request and response packets (hint: filter `TCP`).
2. **(3 pts)** Identify the socket addresses of both the TCP server and client.
3. **(1 pt)** Screenshot of the packet where the client sends a message to the server.
4. **(1 pt)** Screenshot of the packet where the server replies to the client.
5. **(15 pts)** Diagram of the socket communication between client and server — direction, ports, IPs (Application + Transport layer only; see Lecture 4, connection-oriented part).
6. **(4 pts)** From your Wireshark capture, identify the **packet numbers** for: the three-way handshake, data transfer, and connection termination.
7. **(10 pts)** Based on that, **draw a TCP packet exchange diagram** showing the key steps, **TCP flags**, and communication directions.

### Section 3: Designing Your Own Network Application (40 points)
This is the largest section. You must **customize the provided TCP or UDP server source code**, replacing the original letter-case transformation logic with **your own application logic** (not just another simple text transform).

> **Note:** Each group must design its own application logic. Directly copying the design or source code from another group is **not permitted**.

Questions to answer:
1. **(10 pts)** Briefly describe your idea for customizing the provided source code.
2. **(10 pts)** Describe the requirements of your network application: its **input, output, and application logic**.
3. **(10 pts)** Based on 3.2, decide which transport-layer protocol (**TCP or UDP**) is more suitable for your application, and **clearly explain your reasoning**.
4. **(1 pt)** Screenshot of the packet where the client sends a message to the server.
5. **(1 pt)** Screenshot of the packet where the server replies to the client.
6. **(8 pts)** Describe a **real-world scenario** where your application could be applied, and explain how it would improve the service in that scenario.

> **HARD CONSTRAINT: Failure to submit the customized source code = ZERO marks for the entire Section 3 (40 points).**

(Per the submission logistics: you only need to customize whichever server — TCP or UDP — matches the protocol you chose for your application; you don't have to customize both. If you also modified the client code for your application, submit that too.)

## Submission Checklist

Submit **three items** as **one combined submission per group**:

1. **One PDF report** — containing all answers, explanations, diagrams, and required screenshots for every question above.
2. **One Wireshark capture file** (`.pcap` / `.pcapng`) — containing the TCP/UDP communication demonstrated in the report.
3. **Customized server Python source code** (`.py`) — for Section 3, whichever of TCP/UDP server you customized; include modified client code too if you changed it.

Additional logistics:
- The submitted PDF report, capture file, and source code must be **consistent with one another**.
- **Only one complete submission per group** is required/accepted.
- The **Group Leader** is responsible for submitting; the **Assistant Leader** may submit on the Group Leader's behalf if the Leader is unable to.
- All group members are expected to participate and contribute, even though only the Leader/Assistant Leader submits.
- Real communication between actual devices over a network is required — **localhost only is NOT accepted** (stated again in the submission logistics).

## Deadline

**23 Sep 2026**
