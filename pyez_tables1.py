from jnpr.junos import Device
from jnpr.junos.op.ethport import EthPortTable
from getpass import getpass
from pprint import pprint
import ipdb

a_device = Device(host="srx2.lasthop.io", user="pyclass", password=getpass())
#Establish netconf conection via ssh tcp port 830
a_device.open()

#ipdb.set_trace()
#Use EthPortable class to pass netconf connection and return name variable ports
ports = EthPortTable(a_device)
# use netconf connection to retrieve ethernet port info that is a dictionary like object data structure
ports.get()

print(ports)
#print(ports.keys())
#pprint(ports.values())
#pprint(ports.items())
