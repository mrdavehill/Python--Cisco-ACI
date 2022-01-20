# python3.8.4
# inputs: host, aaep and description
# dependencies: none
# created 14-may-2021

class Aaep:

    def __init__(self, apic, aaep, descr):
        self.apic = apic
        self.aaep = aaep
        self.descr = descr
        self.payload = {"infraInfra":{"attributes":{"dn":"uni/infra"},"children":[{"infraAttEntityP":{"attributes":{"dn":"uni/infra/attentp-" + self.aaep,"name":self.aaep,"descr":self.descr,"rn":"attentp-" + self.aaep}}},{"infraFuncP":{"attributes":{"dn":"uni/infra/funcprof"}}}]}}

    def __str__(self):
        return self.apic + '/api/node/mo/uni/infra.json'
'''
{"infraInfra":{"attributes":{"dn":"uni/infra"},"children":[{"infraAttEntityP":{"attributes":{"dn":"uni/infra/attentp-" + self.aaep,"name":self.aaep,"descr":self.descr,"rn":"attentp-" + self.aaep}}},{"infraFuncP":{"attributes":{"dn":"uni/infra/funcprof"}}}]}}
'''