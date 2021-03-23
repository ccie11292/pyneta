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

devices = [device1, device2,]


for device in devices:
    net_connect = ConnectHandler(**device)
    print(net_connect.find_prompt())
    output = net_connect.send_config_from_file(config_file="class2-5_changes.txt")
    output += net_connect.save_config()
    print(output)
    net_connect.disconnect()


