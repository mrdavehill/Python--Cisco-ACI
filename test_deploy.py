# python3.8.4
# inputs: var.py
# dependencies: none
# created 9-may-2021

import unittest
import requests
from requests.packages import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
import sys
sys.path.insert(1, 'classes/APIC4_1_1k')
from var import *
from var import tenant_id
from var import descr_id
from var import username
from var import password
from var import ref_id
from var import vrf_id
from cookies import Cookies
from snapshot import Snapshot
from tenant import Tenant
from vrf import Vrf
import json
import pprint
from run import run


class apicDeploy(unittest.TestCase):

    def setUp(self):
        data = Cookies(apic, username, password)
        push  = requests.post(data, data=json.dumps(data.payload), verify=False)
        self.cookies = push.cookies

    def test_createSnapshot(self):
        data = Snapshot(apic, ref_id)
        push = run(data, data.payload, self.cookies)
        self.assertEqual(push, 200)

    def test_deployTenant(self):
        data = Tenant(apic, tenant_id, descr_id)
        push = run(data, data.payload, self.cookies)
        self.assertEqual(push, 200)

    def test_deployVrf(self):
        data = Vrf(apic, tenant_id, vrf_id, descr_id)
        push = run(data, data.payload, self.cookies)
        self.assertEqual(push, 200)

if __name__ == '__main__':
    unittest.main()