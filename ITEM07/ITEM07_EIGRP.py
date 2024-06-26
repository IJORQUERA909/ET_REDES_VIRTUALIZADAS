from netmiko import ConnectHandler

device = {
    'device_type': 'cisco_ios',
    'host': '192.168.1.136',
    'username': 'cisco',
    'password': 'cisco123!',
}

eigrp_name = "EIGRP-ET"
eigrp_ipv4_configuration = [
    'router eigrp ' + eigrp_name,
    'address-family ipv4 unicast autonomous-system 666',
    'af-interface default',
    'no passive-interface',
    'exit-af-interface',
    'network 10.0.0.0 0.0.0.255',
    'network 192.168.1.0 0.0.0.255',
    'exit-address-family',
]

eigrp_ipv6_configuration = [
    'ipv6 unicast',
    f'router eigrp {eigrp_name}',
    'address-family ipv6 unicast autonomous-system 669',
    'af-interface default',
    'no passive-interface',
    'exit-af-interface',
    'network 2001:db8:1::/64',
    'network 2001:db8:2::/64',
    'exit-address-family'
]


net_connect = ConnectHandler(**device)
net_connect.enable()
net_connect.config_mode()


output_ipv4 = net_connect.send_config_set(eigrp_ipv4_configuration)
print("IPv4 EIGRP Configuration Output:\n", output_ipv4)


output_ipv6 = net_connect.send_config_set(eigrp_ipv6_configuration)
print("IPv6 EIGRP Configuration Output:\n", output_ipv6)


verification_ipv4 = net_connect.send_command('show run | section router eigrp')
print("Verification Output for IPv4 EIGRP:\n", verification_ipv4)

verification_ipv6 = net_connect.send_command('show run | section router eigrp')
print("Verification Output for IPv6 EIGRP:\n", verification_ipv6)


net_connect.disconnect()