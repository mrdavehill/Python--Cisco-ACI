# python3.8.4
# inputs: host, payload and cookies
# dependencies: getCookies.py
# created 9-may-2021

import requests
requests.packages.urllib3.disable_warnings()
import json

def read(url, data, cookies):
    read = requests.get(url, data=json.dumps(data), verify=False, cookies=cookies)
    x = read.status_code
    return x

def write(url, data, cookies):
    write = requests.post(url, data=json.dumps(data), verify=False, cookies=cookies)
    x = write.status_code
    return x

def destroy(url, data, cookies):
    destroy = requests.delete(url, data=json.dumps(data), verify=False, cookies=cookies)
    x = destroy.status_code
    return x