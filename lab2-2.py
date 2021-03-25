from netmiko import ConnectHandler
from getpass import getpass
import time

device = {
    "host": 'nxos2.lasthop.io',
    "username": 'pyclass',
    "password": getpass(),
    "device_type": 'cisco_nxos',
    "global_delay_factor": 2,
    "session_log": 'my_session2-2.txt',
}

net_connect = ConnectHandler(**device)
print(net_connect.find_prompt())

start_time = time.time()
output = net_connect.send_command("show lldp neighbors detail")
print(output)
print("Run time: %s" %(time.time() - start_time))
print("======================")

start_time = time.time()
output = net_connect.send_command("show lldp neighbors detail", delay_factor=8)
print(output)
print("Run time: %s" %(time.time() - start_time))

