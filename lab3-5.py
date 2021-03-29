import yaml
from netmiko import ConnectHandler
#from os import path


#home_dir = path.expanduser("~")
#filename = path.join(home_dir, ".netmiko.yml")

filename = input("Enter filename: ")
with open(filename) as f:
    yaml_out = yaml.load(f)
print(yaml_out)

cisco3 = yaml_out["cisco3"]
net_connect = ConnectHandler(**cisco3)

print()
print(net_connect.find_prompt())
print()

net_connect.disconnect()
