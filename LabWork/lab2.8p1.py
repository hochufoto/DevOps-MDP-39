from ncclient import manager
import xml.dom.minidom
m = manager.connect(
    host = "192.168.10.17",
    port = 830,
    username = "cisco",
    password = "cisco123!",
    hostkey_verify = False
)
netconf_replay = m.get_config(source = "running")
#print(netconf_replay)
print(xml.dom.minidom.parseString(netconf_replay.xml).toprettyxml())

netconf_filter = """
<filter>
    <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native" />
</filter> 
"""

netconf_replay = m.get_config(source="running", filter=netconf_filter)
print(xml.dom.minidom.parseString(netconf_replay.xml).toprettyxml())
