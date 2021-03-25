from netmiko import ConnectHandler
from getpass import getpass
import time

password=getpass()

device = {
    "host": 'cisco4.lasthop.io',
    "username": 'pyclass',
    "password": password,
    "secret": password,
    "device_type": 'cisco_ios',
    "session_log": 'my_session2-6.txt',
}

# a
net_connect = ConnectHandler(**device)
print(net_connect.find_prompt())

# b
net_connect.config_mode()
print(net_connect.find_prompt())

# c
net_connect.exit_config_mode()
print(net_connect.find_prompt())

# d and e
net_connect.write_channel("disable\n")
time.sleep(2)
print(net_connect.read_channel())

# f
net_connect.enable()
print(net_connect.find_prompt())

net_connect.disconnect()


