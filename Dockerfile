FROM python:3.8
RUN python -m pip install \
        requests \ 
        json \
        unittest \
        pytest

#docker run -it -v ~/Python--Cisco-ACI:/code aci python /code/testDrive.py