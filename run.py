# python3.8.4
# inputs: host, payload and cookies
# dependencies: getCookies.py
# created 9-may-2021

import requests
requests.packages.urllib3.disable_warnings()
import json

def run(url, data, cookies):
    run = requests.post(url, data=json.dumps(data), verify=False, cookies=cookies)
    x = run.status_code
    return x