# python3.8.4
# inputs: var.py
# dependencies: none
# created 9-may-2021

import unittest
from var import *
from cookies import Cookies
from snapshot import Snapshot
from tenant import Tenant
from bridge_domain import Bridge_domain
from vrf import Vrf
from vlan_pool import Vlan_pool


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

    def test_apicClassBridge_domain(self):
        bridge_domain = Bridge_domain(apic, tenant_id, bridge_domain_id, subnet_a, vrf_id, descr_id)
        self.assertTrue(isinstance(bridge_domain.payload, dict))

    def test_apicVlan_pool(self):
        vlan_pool = Vlan_pool(apic, vlan_pool_id, vlan_range_start, vlan_range_finish, descr_id)
        self.assertTrue(isinstance(vlan_pool.payload, dict))

if __name__ == '__main__':
    unittest.main()