import json
import requests
requests.packages.urllib3.disable_warnings()
api_url = "https://192.168.10.17/restconf/data/ietf-interfaces:interfaces"
headers = { 
    "Accept": "application/yang-data+json",
    "Content-type":"application/yang-data+json"
}
basicauth = ("cisco", "cisco123!")
resp = requests.get(api_url, auth=basicauth, headers=headers, verify=False)
responce_json = resp.json()
print(json.dumps(responce_json, indent=4))