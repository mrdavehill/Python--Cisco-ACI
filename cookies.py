from json import json.dumps
from requests import requests.post
from var import apic
from credentials import *

class Cookies:

  def __init__(self, apic, username, password):
      self.apic = apic
      self.username = username
      self.password = password

  def get_cookies(self):
      url = apic + '/api/aaaLogin.json'
      auth = {'aaaUser': {'attributes': {'name': credentials.username, 'pwd': credentials.password}}}
      authenticate = requests.post(url, data=json.dumps(auth), verify=False)
      return authenticate.cookies    
