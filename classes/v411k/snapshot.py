# python3.8.4
# inputs: host and unique reference
# dependencies: getCookies.py
# created 9-may-2021


class Snapshot:
    
    def __init__(self, apic, ref):
        self.apic = apic
        self.ref = ref
        self.payload = {'configExportP': {'attributes': {'dn': 'uni/fabric/configexp-defaultOneTime','adminSt': 'triggered','descr': self.ref}}}

    def __str__(self):
        return self.apic + '/api/node/mo/uni/fabric/configexp-defaultOneTime.json'