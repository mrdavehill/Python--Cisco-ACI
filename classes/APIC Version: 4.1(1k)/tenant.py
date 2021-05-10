# python3.8.4
# Cisco Application Policy Infrastructure Controller Version: 4.1(1k)
# inputs: url, tenant and description
# created 9-may-2021

class Tenant:

    def __init__(self, apic, tenant, descr):
        self.apic = apic
        self.tenant = tenant
        self.descr = descr
        self.payload = {"fvTenant":{"attributes":{"descr":self.descr,"dn":"uni/tn-" + self.tenant,"name":self.tenant,"rn":"tn-" + self.tenant}}}

    def __str__(self):
        return self.apic + f'/api/node/mo/uni/tn-{self.tenant}.json?query-target=self'