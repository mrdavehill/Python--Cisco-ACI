from json import dumps
from requests import post, packages
from var import apic
from credentials import username, password


class Cookies:
    
    path = '/api/aaaLogin.json'

    def __init__(self, apic, username, password):
        self.apic = apic
        self.username = username
        self.password = password

    def get_cookies(self, cookies):
        url = self.apic + cookies.path
        body = {'aaaUser': {'attributes': {'name': self.username, 'pwd': self.password}}} 
        authenticate = requests.post(url, data=json.dumps(body), verify=False)
        return authenticate.cookies    
