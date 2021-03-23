from netmiko import ConnectHandler
from getpass import getpass

device = {
    "host":'cisco4.lasthop.io',
    "username":'pyclass',
    "password":getpass(),
    "device_type":'cisco_ios',
    "session_log":'my_session2-1a.txt',
}

net_connect = ConnectHandler(**device)

output = net_connect.send_command_timing("ping")
output += net_connect.send_command_timing("\n")
output += net_connect.send_command_timing("8.8.8.8")
output += net_connect.send_command_timing("\n")
output += net_connect.send_command_timing("\n")
output += net_connect.send_command_timing("\n")
output += net_connect.send_command_timing("\n")
output += net_connect.send_command_timing("\n")

print(output)

