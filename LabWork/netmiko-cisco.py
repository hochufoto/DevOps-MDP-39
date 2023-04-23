from netmiko import ConnectHandler

sshCli = ConnectHandler(
    device_type ="cisco_ios",
    host = "192.168.10.17",
    port = 22,
    username = "cisco",
    password = "cisco123!"
)
 
output = sshCli.send_command("show ip interface brief")
print("show ip interface: \n {}\n".format(output))

config_commands = [
    "interface loopback 1",
    "ip address 2.2.2.1 255.255.255.0",
    "description WHATEVER"
]

output = sshCli.send_config_set(config_commands)
print("config output from device: \n {}\n".format(output))

config_commands = [
    "interface loopback 2",
    "ip address 3.3.3.1 255.255.255.0",
    "description WHATEVER2"
]

output = sshCli.send_config_set(config_commands)
print("config output from device: \n {}\n".format(output))

output = sshCli.send_command("show ip interface brief")
print("show ip interface: \n {}\n".format(output))
