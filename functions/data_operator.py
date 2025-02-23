## DBにデータ登録を行う
import json, os
import inflect

# 取得したデータを単数形、記載揺れを抑える→保存
class DataOperator:
    def __init__(self):
        self.meals_list = []

    # def get_meal_list(self):
    #     self.datas_meal = self.read_datas(f"{self.dir_output}/meals.json")
    #     for data in self.datas_meal:
    #         recipe = Recipe()
    #         recipe.meal_name = data["meal_name"]
    #         recipe.area = data["area"]
    #         recipe.category = data["category"]
    #         recipe.recipe = data["recipe"]
    #         recipe.image_url = data["image_url"]
    #         recipe.ingredients = data["ingredients"]
    #         self.meals_list.append(recipe)
    #     return self.meals_list

    def read_json(self, file_path):
        with open(file_path, "r") as f:
            self.meals_list = json.load(f)

    # 食材データを収集
    # 重複を削除
    def arrange_ingredients(self, file_path):
        self.read_json(file_path)
        ingredients_list = []
        for meal in self.meals_list:
            ingredients_list.extend(meal["ingredients"])
        ingredients_list = list(set(ingredients_list))
        print(ingredients_list)

    
    def plural_to_singular(self, word_list):
        # ホワイトリスト
        white_list = ["octopus"]
        # inflectエンジンのインスタンスを作成
        p = inflect.engine()
        # 単数形のリストを作成
        singular_list = []
        for word in word_list:
            if word.lower() in white_list:
                singular_list.append(word.lower())
                continue

            singular_word = p.singular_noun(word)
            if singular_word:
                singular_list.append(singular_word.lower())
            else:
                singular_list.append(word.lower())
        return singular_list


    def convert_datas_to_singular(self, ingredients):
        # 辞書型データを呼び出す
        for key, content in recipe_database.items():
            # 単数形に変換
            # print(content)
            singulars = self.plural_to_singular(content)
            ingredients[key] = singulars
        return ingredients
        

if __name__ == "__main__":
    dir_current = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    data_operator = DataOperator()
    data_operator.arrange_ingredients(f"{dir_current}/dir_meal_information/meals.json")
    # print(data_operator.meals_list)