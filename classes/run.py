
from tenant import Tenant
from create import create
from cookies import Cookies
import requests
requests.packages.urllib3.disable_warnings()
import json
import pprint
from datetime import datetime

apic = 'https://sandboxapicdc.cisco.com'

def create(url, payload, cookies):
    result = requests.post(url, data=json.dumps(tenant.payload), verify=False, cookies=cookies)
    text = json.loads(result.text)
    code = result.status_code
    pprint.pprint(tenant.payload)
    if code == 200:
        print('\nReturn 200.')
    else:
        print('\nReturn {0}, failed.'.format(code))
        pprint.pprint(text)
        quit()

def get_cookies(username, password):
    url = apic + '/api/aaaLogin.json'
    auth = {'aaaUser': {'attributes': {'name': username, 'pwd': password}}}
    authenticate = requests.post(url, data=json.dumps(auth), verify=False)
    return authenticate.cookies

if __name__ == '__main__':

    now = str(datetime.now().isoformat(timespec='minutes'))
    #cookies = Cookies(apic,)
    cookies = get_cookies('admin', 'ciscopsdt')
    tenant_name = 'tenant'
    descr = 'unittest--' + str(now)

    tenant = Tenant(apic, tenant_name, descr)
    #pprint.pprint(tenant.payload.__dict__)
    print(tenant)
    pprint.pprint(tenant.payload)
    create(tenant, tenant.payload, cookies)