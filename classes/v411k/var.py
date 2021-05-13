# python3.8.4
# inputs: none
# dependencies: none
# created 9-may-2021

import random
unique_name = 'python3--' + str(random.randint(0,999))

apic = 'https://sandboxapicdc.cisco.com'
username = 'admin'
password = 'ciscopsdt'
ref_id = unique_name
descr_id = unique_name
tenant_id = unique_name
vrf_id = unique_name
bridge_domain_id = unique_name
subnet_a = '10.255.255.1/24'
vlan_range_start = '300'
vlan_range_finish = '399'
vlan_pool_id = 'vlan_pool_' + unique_name


