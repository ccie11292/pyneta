import json
from pprint import pprint

#filename = input("Input filename: ")
filename = "lab3-4.json"
with open(filename) as f:
    data = json.load(f)
pprint(data)

arp_dict = {}
arp_entries = data["ipV4Neighbors"]
for entry in arp_entries:
    ip_addr = entry["address"]
    mac_addr = entry["hwAddress"]
    arp_dict[ip_addr] = mac_addr

print()
pprint(arp_dict)
print()
