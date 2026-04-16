# 📡 Network Packet Sniffer (Python + Scapy)

A simple **network packet sniffer** built using Python and the powerful **Scapy** library.  
This tool captures live network traffic and displays useful information such as protocol, source/destination IP, ports, packet length, and a preview of payload data.

---

## 🚀 Features

- 📥 Captures live network packets
- 🌐 Supports:
  - TCP
  - UDP
  - ICMP
  - IPv4 & IPv6
- 🕒 Displays timestamp for each packet
- 🔍 Shows:
  - Source IP & Port
  - Destination IP & Port
  - Protocol type
  - Packet length
- 📄 Payload preview (first 160 characters)
- ♾ Continuous sniffing (until stopped manually)

---

## 🛠 Requirements

- Python 3.x
- Scapy library

Install dependencies:

```bash
pip install scapy
```

---

## ▶️ How to Run

```bash
python sniffer.py
```

> ⚠️ Run as **Administrator/root** for proper packet capturing.

---

## 📌 Example Output

```text
[2026-04-17 01:30:12.123] TCP 192.168.1.5:52344 -> 142.250.183.206:443 | len=60 bytes
[2026-04-17 01:30:13.456] UDP 192.168.1.5:5353 -> 224.0.0.251:5353 | len=78 bytes
```

---

## ⚙️ How It Works

- Uses Scapy’s `sniff()` function to capture packets
- Extracts:
  - IP/IPv6 addresses
  - Protocol (TCP/UDP/ICMP)
  - Ports
- Reads payload using `Raw` layer
- Displays formatted output in real-time

---

## 📂 Project Structure

```text
.
├── sniffer.py   # Main packet sniffing script
└── README.md    # Project documentation
```

---

## ⚠️ Important Notes

- Some payload data may appear unreadable (encrypted traffic like HTTPS)
- Works best on **Linux or Windows with admin privileges**
- Continuous capture may consume system resources over time

---

## 📚 Learning Purpose

This project is useful for:
- Understanding network traffic
- Learning packet structure
- Practicing cybersecurity basics
- Working with Scapy

---

## 🚧 Future Improvements

- Add packet filtering (HTTP, DNS, TCP flags)
- Save logs to file (CSV/JSON)
- GUI interface
- Real-time traffic analysis dashboard

---

## 👨‍💻 Author

Majid Magsi

---

## 📜 License

This project is open-source and free to use for educational purposes.
