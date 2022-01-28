from netmiko import ConnectHandler

device1 = {
	"host": 'cisco3.lasthop.io', 
	"username": 'pyclass', 
	"password": '88newclass', 
	"device_type": 'cisco_ios', 
	# "session_log": 'my_session.txt',	
}
	
net_connect = ConnectHandler(**device1)
print(net_connect.find_prompt())

output = net_connect.send_command("show ip int brief")
print(output)
