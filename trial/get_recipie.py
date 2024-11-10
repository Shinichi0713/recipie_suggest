# 参考URL : https://qiita.com/run1000dori/items/7ffa7907a6c03c8909fc

import requests
import json
from pprint import pprint

applicationid = '1015534497286307304'

def get_recipie_list():
    res = requests.get(f'https://app.rakuten.co.jp/services/api/Recipe/CategoryList/20170426?applicationId={applicationid}')

    json_data = json.loads(res.text)
    pprint(json_data)

def get_recipie_detail(recipie_id):
    res = requests.get(f'https://app.rakuten.co.jp/services/api/Recipe/CategoryRanking/20170426?applicationId={applicationid}&categoryId={recipie_id}')

    json_data = json.loads(res.text)
    pprint(json_data)


def get_etail_food_api():
    res = requests.get(f'https://world.openfoodfacts.net/api/v2/product/3017624010701')

    json_data = json.loads(res.text)
    pprint(json_data)

if __name__ == '__main__':
    recipie_id = '31-720-2130'     # 親id - 自身のカテゴリid
    # get_recipie_list()
    # get_recipie_detail(recipie_id)
    get_etail_food_api()