# python3.8.4
# Cisco Application Policy Infrastructure Controller Version: 4.1(1k)
# inputs: host, username and password
# created 10-may-2021

class Cookies:

    def __init__(self, apic, username, password):
        self.apic = apic
        self.username = username
        self.password = password
        self.payload = {'aaaUser': {'attributes': {'name': self.name, 'pwd': self.password}}} 

    def __str__(self):
        return self.apic + '/api/aaaLogin.json'