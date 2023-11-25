import market
import requests
import json
from com.cosfo.automate.login import login
from com.cosfo.automate.supplier import supplier


# 新建无仓商品
def create_no_warehouse_item(token, title, price):
    # 先创建market 获取market_id
    market_id = market.create_market(token, title, None, None)
    # 无货商品需要供应商信息
    supplier_id, supplier_name = supplier.query_supplier_page(token)

    url = 'https://devmanage.cosfo.cn/market/item/upsert/add'
    headers = {
        "User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/118.0.0.0 Safari/537.36',
        "Content-Type": 'application/json',
        "token": token
    }
    params = {
        "goodsType": 0,
        "marketId": market_id,
        "amount": 10000,
        "onSale": 1,
        "specificationUnit": "箱",
        "miniOrderQuantity": 1,
        "afterSaleUnit": "箱",
        "maxAfterSaleAmount": 1,
        "itemSaleMode": 0,
        "noGoodsSupplyPrice": 1,
        "defaultPrice": {
            "priceType": 1,
            "type": 2,
            "mappingNumber": price,
            "totalStoreCount": 2,
            "differenceValue": 0
        },
        "storeGroupPrice": [],
        "storePrice": [],
        "marketItemUnfairPriceStrategyDTO": {
            "defaultFlag": 1,
            "strategyType": 0
        },
        "saleLimitRule": 0,
        "supplierName": supplier_name,
        "supplierId": supplier_id,
        "specification": "0_1箱*12个"
    }

    json_params = json.dumps(params)
    response = requests.post(url=url, headers=headers, data=json_params)
    if response.status_code != 200:
        raise Exception(f'新建商品: {title}失败')
    else:
        print(f'新建商品: {title}成功')


if __name__ == '__main__':
    token = login.login('15605658291', 'hello1234', 24593)
    create_no_warehouse_item(token, '乔治自动化无仓商品', 1)
