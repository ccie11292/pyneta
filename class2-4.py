from netmiko import ConnectHandler
from getpass import getpass
import time

device = {
    "host": 'cisco3.lasthop.io',
    "username": 'pyclass',
    "password": getpass(),
    "device_type": 'cisco_ios',
    "session_log": 'my_session2-4.txt',
    "fast_cli": True,
}


cfg = [
    'ip name-server 1.1.1.1',
    'ip name-server 1.0.0.1',
    'ip domain-lookup',
]

start_time = time.time()
net_connect = ConnectHandler(**device)
print(net_connect.find_prompt())
print("Run time: %s" %(time.time() - start_time))


start_time = time.time()
output = net_connect.send_config_set(cfg)
print(output)
print("Run time: %s" %(time.time() - start_time))

net_connect.disconnect()

