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


def get_detail_food_api():
    res = requests.get(f'https://world.openfoodfacts.net/api/v2/product/3017624010701')
    json_data = json.loads(res.text)
    pprint(json_data)


def get_sample_api():
    url_target = "https://world.openfoodfacts.net/api/v2/product/3017624010701"
    res = requests.get(url_target)
    json_data = json.loads(res.text)
    pprint(json_data["product"]["ecoscore_data"]["agribalyse"]["name_en"])
    pprint(json_data["product"]["ingredients_text"])




if __name__ == '__main__':
    get_sample_api()