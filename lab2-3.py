from netmiko import ConnectHandler
from getpass import getpass
import time

device = {
    "host": 'cisco4.lasthop.io',
    "username": 'pyclass',
    "password": getpass(),
    "device_type": 'cisco_ios',
    "session_log": 'my_session2-3.txt',
}

net_connect = ConnectHandler(**device)
print(net_connect.find_prompt())

start_time = time.time()
output_version = net_connect.send_command("show version", use_textfsm=True)
print(output_version)
print("Run time: %s" %(time.time() - start_time))
print("======================")

start_time = time.time()
output_lldp = net_connect.send_command("show lldp neighbors", use_textfsm=True)
print(output_lldp)
print("Run time: %s" %(time.time() - start_time))

print("======================")
print(output_lldp[0]["local_interface"])

net_connect.disconnect()

