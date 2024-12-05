# ghost_client
Purple Team tool to generate fake Directed Probe Requests from randomized Wi-Fi clients

# Context.

When your smartphone or favorite device connects to a Wi-Fi network, it stores this network in its memory. This allows it to recognize it and reconnect to it automatically. However, when your device is no longer in the radio coverage area of ​​your access point, it will scan the channels on which it is compatible to receive Beacon frames from surrounding APs and emit Probe Requests.
Depending on the context related to your device's OS, it may search for known networks stored in its memory by emitting frames called Directed Probe Requests, despite the randomization of the MAC address. This process allows a client to detect a known AP more quickly to reconnect to it. However, this poses an obvious security problem.
As part of the animation of an event, I wanted to show this phenomenon. Since not all smartphone, computer, etc. OSs react the same way and to save me time, I decided to develop a script myself to generate a ghost client that sends Directed Probe Requests at regular intervals to an SSID that you have entered.
This script would also allow you to test your Wi-Fi sensor in its ability to visualize this type of information, if you do not have vulnerable client devices.

# Language

The project is based on the Python programming language. For this, I used the scapy library, which is fully functional for the need. I am not a professional developer, so my algorithm is that of a novice.

# Environment.

The script was developed to work on a Raspberry Pi and its Raspberry Pi OS. Modifications are certainly to be expected depending on your context.

line 41. The interface is directly coded in the script. You're supposed to change it according to your context.

line 44. The SSID is directly coded in the script. You're supposed to change it according to your context.

line 47. The channels used are 2,4 GHz ones. You can easily change it according to your need.
