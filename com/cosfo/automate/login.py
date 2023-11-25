import json
import requests


def login(uname, pwd, tid):
    url = 'https://devmanage.cosfo.cn/tenant/user/query/login'

    param = {'phone': uname, 'password': pwd, 'tenantId': tid}
    json_data = json.dumps(param)

    headers = {
        "User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/118.0.0.0 Safari/537.36',
        "Content-Type": 'application/json'
    }
    resp = requests.post(url=url, data=json_data, headers=headers)
    resp_data = resp.json()
    if resp.status_code != 200:
        raise Exception(f'调用登录接口失败，详细原因: {resp_data}')
    else:
        data = resp_data['data']
        token = data['token']
        print(f'调用登录接口成功，获取到token: {token}')
        return token


if __name__ == '__main__':
    username = '13732211112'
    password = '123456'
    tenant_id = 2
    token = login(username, password, tenant_id)
