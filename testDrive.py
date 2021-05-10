# python3.8.4
# inputs: host, payload and cookies
# dependencies: getCookies.py
# created 9-may-2021

import requests
from requests.packages import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
import json

if __name__ == '__main__':