from netmiko import ConnectHandler
from getpass import getpass

cisco3 = {
	'host': 'cisco3.lasthop.io', 
	'username': 'pyclass', 
	'password': getpass(), 
	#'device_type': 'cisco_ios'
}

net_connect = ConnectHandler(**cisco3)
print(net_connect.find_prompt())
output = net_connect.send_command("show arp")

print(output)

with open('show_arp.txt', 'w') as f:
    f.write(output)

net_connect.disconnect()
