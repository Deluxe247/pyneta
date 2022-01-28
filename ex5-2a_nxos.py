from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment

env = Environment(undefined=StrictUndefined)
env.loader = FileSystemLoader('./templates')

interface = 'Ethernet1/1'

nxos1_vars = {
    'interface': interface,
	'ipv4_address': '10.1.100.1',
	'ipv4_netmask': 24
}

nxos2_vars = {
	'interface': interface,
	'ipv4_address': '10.1.100.2',
	'ipv4_netmask': 24
}

for k in (nxos1_vars, nxos2_vars):
    template_file = 'ex5-2a_nxos.j2'
    template = env.get_template(template_file)
    ### render the template
    output = template.render(**k)
    print(output)
    print(k)
