
from scapy.all import sniff, IP, IPv6, TCP, UDP, ICMP, Raw
from datetime import datetime

# count=0 means continuous
PACKET_COUNT = 0
PAYLOAD_PREVIEW_LEN = 160 

def human_ts():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]

def parse_packet(pkt):
    ts = human_ts()
    src = pkt[IP].src if IP in pkt else (pkt[IPv6].src if IPv6 in pkt else "N/A")
    dst = pkt[IP].dst if IP in pkt else (pkt[IPv6].dst if IPv6 in pkt else "N/A")

    proto = "OTHER"
    sport = dport = "-"
    if TCP in pkt:
        proto = "TCP"
        sport = pkt[TCP].sport
        dport = pkt[TCP].dport
    elif UDP in pkt:
        proto = "UDP"
        sport = pkt[UDP].sport
        dport = pkt[UDP].dport
    elif ICMP in pkt:
        proto = "ICMP"

    # Payload is acutal data being transmitted in packet
    payload = ""
    if Raw in pkt:
        raw_bytes = bytes(pkt[Raw].load)
        try:
            payload = raw_bytes.decode('utf-8', errors='replace') # UTF-8 decodes encrypted data
        except:
            payload = str(raw_bytes)

    payload_preview = payload[:PAYLOAD_PREVIEW_LEN].replace("\n", "\\n").replace("\r", "\\r")

    summary = f"[{ts}] {proto} {src}:{sport} -> {dst}:{dport} | len={len(pkt)} bytes"
    if payload_preview:
        summary += f" | payload_preview={payload_preview!r}"
    print(summary)

def main():
    print("Starting packet capture (Ctrl-C to stop)...")
    print("Showing timestamp, protocol, src:port -> dst:port, length and payload preview.")
    sniff(prn=parse_packet, count=PACKET_COUNT, store=False)  # store=False to avoid memory growth

if __name__ == "__main__":
    main()