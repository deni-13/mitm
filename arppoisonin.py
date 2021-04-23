import scapy.all as scapy
arp_response=scapy.ARP()
scapy.ls(scapy.ARP())

#ARP cevabı olusturmak icin op =2 olmalı