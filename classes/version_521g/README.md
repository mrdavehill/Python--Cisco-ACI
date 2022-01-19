## Python--Cisco-ACI/classes/v411k -- Application Policy Infrastructure Controller Version: 5.2(1g)

On this page:

Cisco aci objects as python classes

test_apicClass.py - unittest unit test - instantiates each class with supplied variables and tests dictionary formatting

var.py - variables used by test_apicClass.py and test_pytestDeploy.py
 
### Use Case Description

Creation and testing of Cisco ACI objects in python and CI/CD practices

### How to test the software

git clone https://github.com/mrdavehill/Python--Cisco-ACI.git

python3 -m pytest -s test_pytestDeploy.py

visit DevNet Sandbox and look for tenant "'python3--' + str(random.randint(0,999))"

### DevNet Sandbox

Cisco has an 'always on' APIC [here](https://sandboxapicdc.cisco.com/). 

username = 'admin'

password = '!v3G@!4@Y'

### Getting help

Hit me up if you have any issues.

### Author

This project was written and is maintained by the following Daves:

* Dave Hill <dave@davehill.org>
* https://www.linkedin.com/in/dave-hill-a5a3601b0/
