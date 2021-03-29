import json
from pprint import pprint

#filename = input("Input filename: ")
filename = "lab3-3.json"
with open(filename) as f:
    data = json.load(f)
pprint(data)

ipv4_list = []
ipv6_list = []


print("\nIPv4 Addresses: {}\n".format(ipv4_list))
print("\nIPv6 Addresses: {}\n".format(ipv6_list))
