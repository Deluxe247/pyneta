from getpass import getpass


cisco3 = {
    "host": "cisco3.lasthop.io",
    "username": "pyclass",
    "password": getpass(),
    "device_type": "cisco_ios",
}

arista1 = {
    "host": "arista1.lasthop.io",
    "username": "pyclass",
    "password": getpass(),
    "device_type": "arista_eos",
}

arista2 = {
    "host": "arista2.lasthop.io",
    "username": "pyclass",
    "password": getpass(),
    "device_type": "arista_eos",
}

srx2 = {
    "host": "srx2.lasthop.io",
    "username": "pyclass",
    "password": getpass(),
    "device_type": "juniper_junos",
}

network_devices = [cisco3, arista1, arista2, srx2]