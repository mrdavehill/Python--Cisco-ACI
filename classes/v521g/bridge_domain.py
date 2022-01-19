# python3.8.4
# inputs: host, tenant and description
# dependencies: none
# created 11-may-2021

class Bridge_domain:

    def __init__(self, apic, tenant, bridge_domain, subnet, vrf, descr):
        self.apic = apic
        self.tenant = tenant
        self.bridge_domain = bridge_domain
        self.subnet = subnet
        self.vrf = vrf
        self.descr = descr
        self.payload = {"fvBD":{"attributes":{"dn":"uni/tn-" + self.tenant + "/BD-" + self.bridge_domain,"name":self.bridge_domain,"descr":self.descr,"rn":"BD-" + self.bridge_domain},"children":[{"fvSubnet":{"attributes":{"dn":"uni/tn-" + self.tenant + "/BD-" + self.bridge_domain + "/subnet-[" + self.subnet + "]","ip":self.subnet,"scope":"public","rn":"subnet-[" + self.subnet + "]"}}},{"fvRsCtx":{"attributes":{"tnFvCtxName":self.vrf}}}]}}


    def __str__(self):
        return self.apic + f'/api/node/mo/uni/tn-{self.tenant}/BD-{self.bridge_domain}.json'