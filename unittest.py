#
#
#

import unittest
import requests
from credentials import *
from var import apic
import Cookies

class CRUDTest(unittest.TestCase):
    def setUp(self):
        # instantiate class and create cookie
        self.apic = apic
        self.username = username 
        self.password = password
        self.body = body
        self.cookies = Cookies(self.apic, self.username, self.password)
        #return cookies

    def create(self):
        # create new object on apic
        result = requests.post(url, data=json.dumps(self.body, verify=False, cookies=self.cookies)
        self.assertEqual(self.result.status_code, 200)

    def test_default_widget_size(self):
        # read new object on apic
        pass

    def test_default_widget_size(self):
        # modify the name
        pass

    def test_default_widget_size(self):
        # delete object
       pass
    
