# python3.8.4
# inputs: var.py
# dependencies: none
# created 9-may-2021

import unittest
from getCookies import getCookies
from create import create
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
from cookies import Cookies
from snapshot import Snapshot
from tenant import Tenant
from post import Post
import json
import pprint


class apicDeploy(unittest.TestCase):

    def setUp(self):
        data = Cookies(apic, username, password)
        run = requests.post(data, data=json.dumps(data.payload), verify=False)
        self.cookies = run.cookies

    def test_createSnapshot(self):
        data = Snapshot(apic, ref_id)
        run = requests.post(data, data=json.dumps(data.payload), verify=False, cookies=self.cookies)
        self.assertEqual(run.status_code, 200)

    def test_deployTenant(self):
        data = Tenant(apic, tenant_id, descr_id)
        run = requests.post(data, data=json.dumps(data.payload), verify=False, cookies=self.cookies)
        self.assertEqual(run.status_code, 200)



if __name__ == '__main__':
    unittest.main()