import json
from pprint import pprint

with open ('nxos_interfaces.json') as f:
  nxos_data = json.load(f)

for ifc, ipaddr_dict in nxos_data.items():
    print('#' *12)
    print(ifc)
    print(ipaddr_dict)
    for ip, addr_info in ipaddr_dict.items():
        print('#' *12)
        print(ip)
        print(addr_info)
        for ip_addr, prefix_dict in addr_info.items():
            print('#' *12)
            print(ip_addr)
            print(prefix_dict)
            for prefix_length in prefix_dict.items():
                print(prefix_dict['prefix_length']) 
