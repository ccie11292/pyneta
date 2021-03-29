import yaml
from netmiko import ConnectHandler
from ciscoconfparse import CiscoConfParse

filename = input("Enter filename: ")
with open(filename) as f:
    yaml_out = yaml.load(f)
print(yaml_out)

cisco4 = yaml_out["cisco4"]
net_connect = ConnectHandler(**cisco4)
show_run = net_connect.send_command("show run")

# When feeding config directly - CiscoConfParse requires a list
cisco_cfg = CiscoConfParse(show_run.splitlines())
interfaces = cisco_cfg.find_objects_w_child(
    parentspec=r"^interface", childspec=r"^\s+ip address"
)

print()
for intf in interfaces:
    print("Interface Line: {}".format(intf.text))
    ip_address = intf.re_search_children(r"ip address")[0].text
    print("IP Address Line: {}".format(ip_address))
    print()
print()


