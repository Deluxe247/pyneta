from netmiko import ConnectHandler

net_connect = ConnectHandler(
	host='cisco3.lasthop.io', 
	username='pyclass', 
	password='88newclass', 
	device_type='cisco_ios', 
	session_log='my_session.txt',
)

print(net_connect.find_prompt())

print('test')

