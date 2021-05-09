#python3.8.4
#
#

class Cookies:
    
    path = '/api/aaaLogin.json'
    body = {'aaaUser': {'attributes': {'name': '', 'pwd': ''}}} 

    def __init__(self, apic, username, password):
        self.apic = apic
        self.username = username
        self.password = password

    def url(self):
        return self.apic + url.path

    def payload(self):
        body['aaaUser']['attributes']['name'] = self.username
        body['aaaUser']['attributes']['pwd'] = self.password
        return body