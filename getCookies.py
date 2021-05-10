# python3.8.4
# inputs: host, username and password
# dependencies: none
# created 9-may-2021

import requests
requests.packages.urllib3.disable_warnings()
import json
import pprint
import sys
sys.path.insert(1, 'classes/APIC4_1_1k')
from cookies import Cookies
from var import *

def getCookies(apic, username, password):
    payload = Cookies(apic, username, password)
    authenticate = requests.post(apic, data=json.dumps(payload), verify=False)
    return authenticate.cookies