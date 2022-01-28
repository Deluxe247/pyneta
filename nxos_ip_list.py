import json

filename = "nxos_interfaces.json"
with open(filename) as f:
    nxos_data = json.load(f)

ipv4_list = []
ipv6_list = []

for intf, ipaddr_dict in nxos_data.items():
    for ipv4_or_ipv6, addr_info in ipaddr_dict.items():
        for ip_addr, prefix_dict in addr_info.items():
            prefix_length = prefix_dict["prefix_length"]
            if ipv4_or_ipv6 == "ipv4":
                ipv4_list.append("{}/{}".format(ip_addr, prefix_length))
            elif ipv4_or_ipv6 == "ipv6":
                ipv6_list.append("{}/{}".format(ip_addr, prefix_length))

print(f'\nIPv4 Addresses: \n{ipv4_list}\n')
print(f'IPv6 Addresses: \n{ipv6_list}\n')

