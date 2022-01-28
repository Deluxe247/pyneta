import time
from netmiko import ConnectHandler
from my_devices import network_devices

def send_show_version(device):
    net_connect =  ConnectHandler(**device)
    return net_connect.find_prompt()
    return net_connect.send_command("show version")

if __name__ == "__main__":  

    show_version = send_show_version(network_devices[0])

    print(show_version)




