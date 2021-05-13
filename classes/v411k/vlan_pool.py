# python3.8.4
# inputs: host, tenant and description
# dependencies: none
# created 12-may-2021

class Vlan_pool:

    def __init__(self, apic, vlan_pool, vlan_range_start, vlan_range_finish, descr):
        self.apic = apic
        self.vlan_pool = vlan_pool
        self.vlan_range_start = vlan_range_start
        self.vlan_range_finish = vlan_range_finish
        self.descr = descr
        self.payload = {"fvnsVlanInstP":{"attributes":{"dn":"uni/infra/vlanns-[" + self.vlan_pool + "]-static","name":self.vlan_pool,"descr":self.descr,"rn":"vlanns-[" + self.vlan_pool + "]-static"},"children":[{"fvnsEncapBlk":{"attributes":{"dn":"uni/infra/vlanns-[" + self.vlan_pool + "]-static/from-[vlan-" + self.vlan_range_start + "]-to-[vlan-" + self.vlan_range_finish + "]","from":"vlan-" + self.vlan_range_start,"to":"vlan-" + self.vlan_range_finish,"rn":"from-[vlan-" + self.vlan_range_start + "]-to-[vlan-" + self.vlan_range_finish + "]"}}}]}}


    def __str__(self):
        return self.apic + f'/api/node/mo/uni/infra/vlanns-[{self.vlan_pool}]-static.json'
