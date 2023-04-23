from ncclient import manager
import xml.dom.minidom
import xmltodict
m = manager.connect(
    host = "192.168.10.17",
    port = 830,
    username = "cisco",
    password = "cisco123!",
    hostkey_verify = False
)
netconf_filter = """
<filter>
    <interfaces-state xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces" />
</filter> 
"""
netconf_replay = m.get(filter=netconf_filter)
#print(xml.dom.minidom.parseString(netconf_replay.xml).toprettyxml())
netconf_replay_dict = xmltodict.parse(netconf_replay.xml)
for interface in netconf_replay_dict["rpc-reply"]["data"]["interfaces-state"]["interface"]:
    print("Name: {} MAC: {} Input: {} Output: {} ".format(
        interface["name"],
        interface["phys-address"],
        interface["statistics"]["in-octets"],
        interface["statistics"]["out-octets"]
        )
    )