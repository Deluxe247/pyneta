import yaml
from netmiko import ConnectHandler

net_connect = ConnectHandler(
        host='cisco3.lasthop.io',
        username='pyclass',
        password='88newclass',
        device_type='cisco_ios',
        session_log='my_session.txt',
)

filename = input("Enter filename: ")
with open(filename) as f:
    yaml_out = yaml.load(f)
print(yaml_out)
