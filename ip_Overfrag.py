#!/usr/bin/python3
from scapy.all import *

# Construct IP header
ip = IP(src="192.168.65.132", dst="192.168.65.131")
ip.id = 1000
ip.frag = 0
ip.flags = 1


# Construct UDP header

udp = UDP(sport=7070, dport=9090)
udp.len = 168 # This should be the combined length of all fragments
# Construct payload
payload = 'A' * 80 # Put 80 bytes in the first fragment
# Construct the entire packet and send it out
pkt = ip/udp/payload # For other fragments, we should use ip/payload
pkt[UDP].checksum = 0 # Set the checksum field to zero
print("Sending fragment: ", pkt.frag)
send(pkt, verbose=0)


ip.frag = 5
payload = 'B' * 80
pkt = ip/udp/payload
pkt[UDP].checksum = 0
send(pkt, verbose=0)
print("Sending fragment: ", pkt.frag)
send(pkt, verbose=0)

ip.frag = 10
ip.flags = 0
payload = 'C' * 80
pkt = ip/udp/payload
pkt[UDP].checksum = 0
send(pkt, verbose=0)
print("Sending fragment: ", pkt.frag)
send(pkt, verbose=0)
