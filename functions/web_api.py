
import requests, json

# theMealDBのAPIを利用して、レシピ情報を取得するクラス
class RecipeAPI:
    def __init__(self):
        self.endpoint = 'https://www.themealdb.com/api/json/v1/1/search.php?'

    def get_meal_list(self):
        data = requests.get(f'{self.endpoint}f=a').json()
        # JSONデータを整形して表示 
        formatted_data = json.dumps(data, indent=4, ensure_ascii=False)
        return formatted_data

    def get_recipie_detail(self, recipie_id):
        res = requests.get(f'https://app.rakuten.co.jp/services/api/Recipe/CategoryRanking/20170426?applicationId={self.applicationid}&categoryId={recipie_id}')
        return res.json()

    def get_detail_food_api(self):
        res = requests.get(f'https://world.openfoodfacts.net/api/v2/product/3017624010701')
        return res.json()

    def get_sample_api(self):
        url_target = "https://world.openfoodfacts.net/api/v2/product/3017624010701"
        res = requests.get(url_target)
        json_data = res.json()
        return json_data["product"]["ecoscore_data"]["agribalyse"]["name_en"], json_data["product"]["ingredients_text"]


if __name__ == '__main__':
    api = RecipeAPI()
    print(api.get_meal_list())
