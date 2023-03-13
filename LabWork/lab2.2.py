from netmiko import ConnectHandler

sshCli = ConnectHandler(
    device_type = 'cisco_ios',
    host = '192.168.10.18',
    port = 22,
    username = 'cisco',
    password = 'cisco123!'
)

output = sshCli.send_command("show ip int brief")
print("show ip int brief:\n{}\n".format(output))

config_commands = [
    'int loopback 1',
    'ip address 2.2.2.2 255.255.255.0',
    'description WHATEVER'
]

config_commands = [
    'int loopback 2',
    'ip address 2.2.2.2 255.255.255.0',
    'description WHATEVER'
]

output = sshCli.send_config_set(config_commands)
print("Config output from the device: \n {} \n".format(output))

output = sshCli.send_command("show ip int brief")
print("show ip int brief:\n{}\n".format(output))
