# python3.8.4
# inputs: host, username and password
# dependencies: 
# created 10-may-2021

import requests
import json

class Post:

    def __init__(self, apic, payload, cookies):
        self.apic = apic
        self.payload = payload
        self.cookies = cookies

    def post(self, apic, payload, **kwargs):
        post = requests.post(self.apic, data=json.dumps(self.payload), verify=False, cookies=self.cookies)
        return post.status_code