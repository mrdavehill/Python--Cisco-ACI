# python3.8.4
# inputs: host, tenant, vrf and description
# dependencies: tenant.py
# created 10-may-2021

class Vrf:

    def __init__(self, apic, tenant, vrf, descr):
        self.apic = apic
        self.tenant = tenant
        self.vrf = vrf
        self.descr = descr
        self.payload = {"fvCtx":{"attributes":{"dn":"uni/tn-" + self.tenant + "/ctx-" + self.vrf,"name":self.vrf,"descr":self.descr,"rn":"ctx-" + self.vrf,}}}

    def __str__(self):
        return self.apic + f'/api/node/mo/uni/tn-{self.tenant}/ctx-{self.vrf}.json'