# python3.8.4
# inputs: host, payload and cookies
# dependencies: getCookies.py
# created 9-may-2021

import requests
requests.packages.urllib3.disable_warnings()
import json
import pprint

def create(url, payload, cookies):
    result = requests.post(url, data=json.dumps(payload), verify=False, cookies=cookies)
    text = json.loads(result.text)
    code = result.status_code
    pprint.pprint(tenant.payload)
    if code == 200:
        print('\nReturn 200.')
    else:
        print('\nReturn {0}, failed.'.format(code))
        pprint.pprint(text)
        quit()