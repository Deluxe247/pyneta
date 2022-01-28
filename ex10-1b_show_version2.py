from netmiko import ConnectHandler
from my_devices import network_devices

def ssh_command(device, command):
    """Est SSH, Execute show command, return results"""
    net_connect =  ConnectHandler(**device)
    output = net_connect.send_command(command)
    net_connect.disconnect()
    return output

def main():
    for device in network_devices:
        output = ssh_command(device,"show version") 
        print("=" * 20)
        print(output) 
        print("\n\n")
    print("=" * 20)

if __name__ == "__main__":  
    main()



    