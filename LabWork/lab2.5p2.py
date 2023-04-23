import json
import requests
requests.packages.urllib3.disable_warnings()
api_url = "https://192.168.10.17/restconf/data/ietf-interfaces:interfaces/interface=Loopback44"
headers = { 
    "Accept": "application/yang-data+json",
    "Content-type":"application/yang-data+json"
}
basicauth = ("cisco", "cisco123!")
yangConfig = {
    "ietf-interfaces:interface": {
        "name": "Loopback44",
        "description": "WHATEVER44",
        "type": "iana-if-type:softwareLoopback",
        "enabled": "true",
        "ietf-ip:ipv4": {
            "address": [
                {
                    "ip": "56.78.99.12",
                    "netmask": "255.255.255.0"
                }
            ]
        },
        "ietf-ip:ipv6": {}
    }
}
resp = requests.put(api_url, data=json.dumps(yangConfig), auth=basicauth, headers=headers, verify=False)
if (resp.status_code >= 200 and resp.status_code <= 299):
    print("Status OK: {}".format(resp.status_code))
else:
    print("Error code: {}, reply: {}".format(resp.status_code, resp.json()))