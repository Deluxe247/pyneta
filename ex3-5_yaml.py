import yaml
from netmiko import ConnectHandler



filename = input("Enter filename: ")

with open(filename) as f:
    yaml_out = yaml.load(f)


cisco3 = yaml_out['cisco3']
net_connect = ConnectHandler(**cisco3)

print()
print(net_connect.find_prompt())
print()
