from netmiko import ConnectHandler

conect = ConnectHandler(
    device_type = 'cisco_ios',
    host = '192.168.1.136',
    port = 22,
    username = 'cisco',
    password = 'cisco123!'
    )

output = conect.send_command("sh running-config")
print(output)



