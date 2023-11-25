from com.cosfo.automate.login import login
import requests
import json
from com.cosfo.automate.market.classification import market_classification


# create a market method
def create_market(token, title, main_pic, classification_id):
    # process params
    if title is None or title == '':
        title = get_default_market_title()
    if main_pic is None or main_pic == '':
        main_pic = get_default_market_main_pic()
    if classification_id is None:
        classification_id = get_default_market_classification(token)

    param = {'title': title, 'mainPicture': main_pic, 'classificationId': classification_id}
    json_data = json.dumps(param)

    url = 'https://devmanage.cosfo.cn/market/upsert/add'
    headers = {
        "User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/118.0.0.0 Safari/537.36',
        "Content-Type": 'application/json',
        "token": token
    }

    response = requests.post(url=url, headers=headers, data=json_data)
    response_json = response.json()
    if response.status_code != 200:
        raise Exception(f'创建商品异常，异常信息：{response}')
    else:
        data = response_json['data']
        market_id = data['marketId']
        print(f'创建{title}成功')
        return market_id


def get_default_market_title():
    title = '自动化测试商品'
    return title


def get_default_market_main_pic():
    main_pic = 'test/8xmgrkb2ziawxn1s.jpeg'
    return main_pic


def get_default_market_classification(token):
    return market_classification.query_first_child_classification(token)


if __name__ == '__main__':
    # login module get token
    token = login.login('15605658291', 'hello1234', 24593)
    print('请输入商品名称，以enter结束：')
    title = input()
    market_id = create_market(token, title, None, None)
