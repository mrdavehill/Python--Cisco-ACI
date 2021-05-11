# python3.8.4
# inputs: var.py
# dependencies: none
# created 9-may-2021

import unittest
import requests
from classes.v411k import *
from classes.v411k.var import *
import json
from actions import write as w, read as r, change as c, destroy as d


class apicDeploy(unittest.TestCase):

    def setUp(self):
        data = cookies.Cookies(apic, username, password)
        push  = requests.post(data, data=json.dumps(data.payload), verify=False)
        self.cookies = push.cookies

    def test_createSnapshot(self):
        data = snapshot.Snapshot(apic, ref_id)
        push = w(data, data.payload, self.cookies)
        self.assertEqual(push, 200)

    def test_deployTenant(self):
        data = tenant.Tenant(apic, tenant_id, descr_id)
        push = w(data, data.payload, self.cookies)
        self.assertEqual(push, 200)

    def test_deployVrf(self):
        data = vrf.Vrf(apic, tenant_id, vrf_id, descr_id)
        push = w(data, data.payload, self.cookies)
        self.assertEqual(push, 200)

    def test_readTenant(self):
        data = tenant.Tenant(apic, tenant_id, descr_id)
        push = r(data, data.payload, self.cookies)
        self.assertEqual(push, 200) 
    
    def test_readVrf(self):
        data = vrf.Vrf(apic, tenant_id, vrf_id, descr_id)
        push = r(data, data.payload, self.cookies)
        self.assertEqual(push, 200)

    def test_updateTenant(self):
        data = tenant.Tenant(apic, tenant_id, descr_id_change)
        push = c(data, data.payload, self.cookies)
        self.assertEqual(push, 200) 

if __name__ == '__main__':
    unittest.main()