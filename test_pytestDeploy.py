#!/usr/bin/python3
# python3.8.4
# inputs: everything
# dependencies: all
# created 11-may-2021

import pytest
import requests
requests.packages.urllib3.disable_warnings()
from classes.v411k import *
from classes.v411k.var import *
import json

@pytest.fixture(scope='session', autouse=True)
def get_cookies():
    url = apic + '/api/aaaLogin.json'
    auth = {'aaaUser': {'attributes': {'name': username, 'pwd': password}}}
    authenticate = requests.post(url, data=json.dumps(auth), verify=False)
    return authenticate.cookies

def test_createSnapshot(get_cookies):
    data = snapshot.Snapshot(apic, ref_id)
    push = requests.post(data, data=json.dumps(data.payload), verify=False, cookies=get_cookies)
    assert push.status_code == 200

def test_deployTenant(get_cookies):
    data = tenant.Tenant(apic, tenant_id, descr_id)
    push = requests.post(data, data=json.dumps(data.payload), verify=False, cookies=get_cookies)
    assert push.status_code == 200

def test_deployVrf(get_cookies):
    data = vrf.Vrf(apic, tenant_id, vrf_id, descr_id)
    push = requests.post(data, data=json.dumps(data.payload), verify=False, cookies=get_cookies)
    assert push.status_code == 200

def test_readTenant(get_cookies):
    data = tenant.Tenant(apic, tenant_id, descr_id)
    push = requests.post(data, data=json.dumps(data.payload), verify=False, cookies=get_cookies)
    assert push.status_code == 200 

def test_readVrf(get_cookies):
    data = vrf.Vrf(apic, tenant_id, vrf_id, descr_id)
    push = requests.post(data, data=json.dumps(data.payload), verify=False, cookies=get_cookies)
    assert push.status_code == 200

def test_deployBridge_domain(get_cookies):
    data = bridge_domain.Bridge_domain(apic, tenant_id, bridge_domain_id, subnet_a, vrf_id, descr_id)
    push = requests.post(data, data=json.dumps(data.payload), verify=False, cookies=get_cookies)
    assert push.status_code == 200

def test_deployBridge_domain(get_cookies):
    data = vlan_pool.Vlan_pool(apic, vlan_pool_id, vlan_range_start, vlan_range_finish, descr_id)
    push = requests.post(data, data=json.dumps(data.payload), verify=False, cookies=get_cookies)
    assert push.status_code == 200
