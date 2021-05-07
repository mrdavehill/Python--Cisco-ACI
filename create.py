#python3.8.4
#
#

def create(url, data, cookies):
    push = requests.post(url, data=json.dumps(payload), verify=False, cookies=cookies)
    text = json.loads(push.text)
    code = push.status_code
    if code == 200:
        print('\nReturn 200, sucess.')
    else:
        print(f'\nReturn {code}, failed.')
        pprint.pprint(text)
        quit()