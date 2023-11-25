import requests
from com.cosfo.automate.login import login


def query_supplier_page(token):
    url = 'https://devmanage.cosfo.cn/pms-service/saas-supplier/list/page'
    headers = {
        "User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/118.0.0.0 Safari/537.36',
        "Content-Type": 'application/json',
        "token": token
    }
    params = {
        "pageIndex": 1,
        "pageSize": 10
    }
    response = requests.post(url=url, headers=headers, json=params)
    if response.status_code != 200:
        raise Exception('查询供应商列表出错')
    response_json = response.json()
    data = response_json['data']
    supplier_list = data['list']
    supplier_info = supplier_list[0]
    return supplier_info['supplierId'], supplier_info['supplierName']


if __name__ == '__main__':
    token = login.login('13732211112', '123456', 2)
    supplier_id, supplier_name = query_supplier_page(token)
