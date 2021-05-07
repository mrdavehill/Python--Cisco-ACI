#python3.8.4
#
#

class Snapshot:
    
    path = '/api/node/mo/uni/fabric/configexp-defaultOneTime.json'
    body = {'configExportP': {'attributes': {'dn': 'uni/fabric/configexp-defaultOneTime','adminSt': 'triggered','descr': ''}}}  

    def __init__(self, apic, ref):
        self.apic = apic
        self.ref = ref

    def url(self):
        return self.apic + url.path

    def payload(self):
        body['configExportP']['attributes']['descr'] = self.ref
        return body