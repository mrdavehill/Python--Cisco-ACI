# python3.8.4
# created 9-may-2021

import unittest
from var import *
#import sys
#sys.path.append('../classes/APIC4_1(k)/')

class apicClass(unittest.TestCase):

    def test_apicClassTenant(self):
        tenant = Tenant(apic, tenant_id, descr_id)
        self.assertTrue(isinstance(tenant.payload, dict))

    def test_apicClassSTR(self):
        # is type STR
        pass

if __name__ == '__main__':
    unittest.main()