from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment

env = Environment(undefined=StrictUndefined)
env.loader = FileSystemLoader('./templates')

interface = 'Ethernet1/1'
asn = 22

nxos1_vars = {
    'interface': interface,
    'ipv4_address': '10.1.100.1',
    'ipv4_netmask': 24,
    'local_as': asn,
    'peer_ip': '10.1.100.2',
    'remote_as': asn
}

nxos2_vars = {
    'interface': interface,
    'ipv4_address': '10.1.100.2',
    'ipv4_netmask': 24,
    'local_as': asn,
    'peer_ip': '10.1.100.1',
    'remote_as': asn
}

for k in (nxos1_vars, nxos2_vars):
    template_file = 'ex5-2b_nxos.j2'
    template = env.get_template(template_file)
    ### render the template
    output = template.render(**k)
    print()
    print(output)
    print()
