# python3.8.4
# inputs: var.py
# dependencies: none
# created 9-may-2021

import unittest
from var import *
from cookies import Cookies
from snapshot import Snapshot
from tenant import Tenant
from vrf import Vrf


class apicClass(unittest.TestCase):

    def test_apicClassCookies(self):
        cookies = Cookies(apic, username, password)
        self.assertTrue(isinstance(cookies.payload, dict))

    def test_apicClassSnapshot(self):
        snapshot = Snapshot(apic, ref_id)
        self.assertTrue(isinstance(snapshot.payload, dict))

    def test_apicClassTenant(self):
        tenant = Tenant(apic, tenant_id, descr_id)
        self.assertTrue(isinstance(tenant.payload, dict))

    def test_apicClassVRF(self):
        vrf = Vrf(apic, tenant_id, vrf_id, descr_id)
        self.assertTrue(isinstance(vrf.payload, dict))

if __name__ == '__main__':
    unittest.main()