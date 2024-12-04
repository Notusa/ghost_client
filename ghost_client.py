from scapy.all import *
import time
import os
import random

def generate_custom_mac():
    # Set the second character of the first byte as 2, 6, A or E
    first_octet_options = ['02','12', '22', '32', '42', '52', '62', '72', '82', '92', 'A2', 'B2', 'C2', 'D2', 'E2', 'F2', '06', '16', '26', '36', '46', '56', '66', '76', '86', '96', 'A6', 'B6', 'C6', 'D6', 'E6', 'F6', '0A', '1A', '2A', '3A', '4A', '5A', '6A', '7A', '8A', '9A', 'AA', 'BA', 'CA', 'DA', 'EA', 'FA', '0E', '1E', '2E', '3E', '4E', '5E', '6E', '7E', '8E', '9E', 'AE', 'BE', 'CE', 'DE', 'EE', 'FE']
    first_octet = random.choice(first_octet_options)

    # Generate the other 5 bytes randomly
    mac = [first_octet]
    for _ in range(5):
        octet = format(random.randint(0, 255), '02x')
        mac.append(octet)
    
    return ':'.join(mac)

def send_directed_probe_request(ssid, iface):
    # Generate a customed MAC address for each request
    # Génération d'une adresse MAC personnalisée pour chaque requête
    random_mac = generate_custom_mac()

    # Build a probe request packet
    dot11 = Dot11(type=0, subtype=4, addr1="ff:ff:ff:ff:ff:ff", addr2=random_mac, addr3="ff:ff:ff:ff:ff:ff")
    probe_req = Dot11ProbeReq()
    essid = Dot11Elt(ID="SSID", info=ssid, len=len(ssid))
    rates = Dot11Elt(ID="Rates", info=b'\x82\x84\x8b\x96\x24\x30\x48\x6c')

    # Build final packet
    packet = RadioTap()/dot11/probe_req/essid/rates

    # Send packet
    sendp(packet, iface=iface, count=1, verbose=False)
    return random_mac

def change_channel(iface, channel):
    os.system(f"sudo iwconfig {iface} channel {channel}")

# Change the interface according to the context
iface = "wlan0mon"

# Set a SSID
target_ssid = "CanUSeeMe?"

# 2,4 GHz channel list
channels = list(range(1, 12))

while True:
    # Choose a channel randomly for each probe request
    current_channel = random.choice(channels)
    change_channel(iface, current_channel)
    mac_used = send_directed_probe_request(target_ssid, iface)

    # Send the probe request
    print(f"Sent Probe Request from {mac_used} on channel {current_channel}")
    time.sleep(20)
