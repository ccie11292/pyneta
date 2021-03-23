from netmiko import ConnectHandler
from getpass import getpass

device = {
    "host":'cisco4.lasthop.io',
    "username":'pyclass',
    "password":getpass(),
    "device_type":'cisco_ios',
    "session_log":'my_session2-1b.txt',
}

net_connect = ConnectHandler(**device)

output = net_connect.send_command("ping", expect_string=":")
output += net_connect.send_command("\n", expect_string=":")
output += net_connect.send_command("8.8.8.8", expect_string=":")
output += net_connect.send_command("\n", expect_string=":")
output += net_connect.send_command("\n", expect_string=":")
output += net_connect.send_command("\n", expect_string=":")
output += net_connect.send_command("\n", expect_string=":")
output += net_connect.send_command("\n", expect_string="#")

print(output)

