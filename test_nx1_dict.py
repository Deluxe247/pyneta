from netmiko import ConnectHandler

devicenx1 = {
	"host": 'nxos1.lasthop.io',
	"username": 'pyclass',
	"password": '88newclass',
	"device_type": 'cisco_nxos',

}

net_connect = ConnectHandler(**devicenx1)
print(net_connect.find_prompt())
