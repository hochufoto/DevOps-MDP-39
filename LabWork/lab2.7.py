from ncclient import manager

m = manager.connect(
    host = "192.168.10.17",
    port = 830,
    username = "cisco",
    password = "cisco123!",
    hostkey_verify = False
)

file = open("./../DevOps-MDP-39_book/2.1.1.3 Lab activities/2.7/lab-2.7-capability.txt", "w")

print("Support Capabilities (YANG models):")
file.write("Support Capabilities (YANG models): \n")

for capability in m.server_capabilities:
    print(capability)
    file.write(capability + "\n")
file.close()
