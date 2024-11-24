
import requests, json

# theMealDBのAPIを利用して、レシピ情報を取得するクラス
class RecipieAPI:
    def __init__(self):
        self.endpoint_search = 'https://www.themealdb.com/api/json/v1/1/search.php?'

    # 料理一覧を取得
    def get_meal_list(self):
        self.meals_list = []
        # 先頭文字をaからzまで取得
        # for i in range(97, 123):
        for i in range(97, 98):
            char_search = chr(i)
            datas = requests.get(f'{self.endpoint_search}f={char_search}').json()
            # JSONデータを整形して表示
            formatted_datas = json.dumps(datas, indent=4, ensure_ascii=False)
            # print(formatted_datas)
            datas = datas["meals"]
            # mealsより料理情報を取得
            for data in datas:
                self.meals_list.append(data["strMeal"])
        print(self.meals_list)
        # return formatted_datas

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
    api = RecipieAPI()
    print(api.get_meal_list())
