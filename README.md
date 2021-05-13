## Python--Cisco-ACI

On this page:

classes/v411k - Cisco ACI objects as python classes for Version: 4.1(1k)

.travis.yml - config file for Travis CI test automation (runs test_pytestDeploy.py on git push)

requirements.txt - lists the required extra python libraries

test_pytestDeploy.py - pytest integration test that will install all the classes in classes/APIC4_1_1k on a DevNet sandbox APIC in dependant order
 
### Use Case Description

Creation and testing of Cisco ACI objects in python and CI/CD practices

### How to test the software

git clone https://github.com/mrdavehill/Python--Cisco-ACI.git

python3 -m pytest -s test_pytestDeploy.py

visit DevNet Sandbox and look for tenant "'python3--' + str(random.randint(0,999))"

### DevNet Sandbox

Cisco has an 'always on' APIC [here](https://sandboxapicdc.cisco.com/). 

username = 'admin'

password = 'ciscopsdt'

### Getting help

Hit me up if you have any issues.

### Author

This project was written and is maintained by the following Daves:

* Dave Hill <dave@davehill.org>
* https://www.linkedin.com/in/dave-hill-a5a3601b0/
