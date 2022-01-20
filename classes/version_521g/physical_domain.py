

create physical domain

method: POST
url: https://sandboxapicdc.cisco.com/api/node/mo/uni/phys-self.physical_domain.json
payload{"physDomP":{"attributes":{"dn":"uni/phys-self.physical_domain","name":"self.physical_domain","rn":"phys-self.physical_domain","status":"created"},"children":[{"infraRsVlanNs":{"attributes":{"tDn":"uni/infra/vlanns-[self.vlan_pool]-static","status":"created"},"children":[]}}]}}
response: {"totalCount":"0","imdata":[]}

