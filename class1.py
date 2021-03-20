from netmiko import ConnectHandler
from getpass import getpass

device1 = {
    "host":'nxos1.lasthop.io',
    "username":'pyclass',
    "password":getpass(),
    "device_type":'cisco_nxos',
    # "session_log":'my_session.txt',
}

device2 = {
    "host":'nxos2.lasthop.io',
    "username":'pyclass',
    "password":getpass(),
    "device_type":'cisco_nxos',
    # "session_log":'my_session.txt',
}

device3 = {
    "host":'cisco1.lasthop.io',
    "username":'pyclass',
    "password":getpass(),
    "device_type":'cisco_ios',
    "session_log":'my_session.txt',
}


devices = [device1, device2, device3]

for device in devices:
    net_connect = ConnectHandler(**device)
    print(net_connect.find_prompt())
    if device["device_type"]=='cisco_ios':
        output = net_connect.send_command("show version")
        print(output)

