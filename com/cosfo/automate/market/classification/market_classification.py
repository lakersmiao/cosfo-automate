import requests
from com.cosfo.automate.login import login
import json


def query_first_child_classification(token):
    url = 'https://devmanage.cosfo.cn/marketClassification/listAll'
    headers = {
        "User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/118.0.0.0 Safari/537.36',
        "token": token
    }
    response = requests.get(url=url, headers=headers)
    response_tex = response.text
    response_dict = json.loads(response_tex)
    response_data = response_dict['data']
    first_classification_dict = response_data[0]
    second_classification_list = first_classification_dict['childList']
    second_classification_dict = second_classification_list[0]
    return second_classification_dict['id']


if __name__ == '__main__':
    token = login.login('15605658291', 'hello1234', 24593)
    first_child_classification_id = query_first_child_classification(token)
    print(f'查询到第一个二级分组id: {first_child_classification_id}')
