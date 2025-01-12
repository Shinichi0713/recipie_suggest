
import requests, json, os


# theMealDBのAPIを利用して、レシピ情報を取得するクラス
class RecipeAPI:
    def __init__(self):
        self.endpoint_search = 'https://www.themealdb.com/api/json/v1/1/search.php?'
        self.dir_output = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/dir_meal_information"

    # 料理一覧を取得
    def get_meal_list(self):
        self.meals_list = []
        # 先頭文字をaからzまで取得
        # for i in range(97, 123):
        for i in range(97, 98):
            char_search = chr(i)
            datas = requests.get(f'{self.endpoint_search}f={char_search}').json()
            # JSONデータを整形して表示
            datas = datas["meals"]
            # mealsより料理情報を取得
            for data in datas:
                recipe = Recipe()
                recipe.meal_name = data["strMeal"]
                recipe.area = data["strArea"]
                recipe.category = data["strCategory"]
                recipe.recipe = data["strInstructions"]
                recipe.image_url = data["strMealThumb"]
                for key in data.keys():
                    if key.startswith("strIngredient"):
                        if data[key] != "" and data[key] is not None:
                            recipe.ingredients.append(data[key])
                self.meals_list.append(recipe)
        self.save_meal_list(f"{self.dir_output}/meals.json")
        print(self.meals_list)

    def save_meal_list(self, file_path):
        with open(file_path, "w") as f:
            json.dump([meal.to_dict() for meal in self.meals_list], f, indent=4)

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

    def read_datas(self, file_path):
        with open(file_path, "r") as f:
            self.datas_meal = json.load(f)
        return self.datas_meal

# レシピ情報を取得するクラス
class Recipe:
    def __init__(self):
        self.meal_name = ""
        self.category = ""
        self.area = ""
        self.recipe = ""
        self.ingredients = []
        self.image_url = ""

    def to_dict(self):
        return self.__dict__
    
    def save(self, file_path):
        with open(file_path, "w") as f:
            json.dump(self.to_dict(), f, indent=4)

    

if __name__ == '__main__':
    api = RecipeAPI()
    print(api.get_meal_list())
    print(api.read_datas(f"{api.dir_output}/meals.json"))
