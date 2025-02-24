## DBにデータ登録を行う
import json, os
import inflect
import db_operator


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

    def __read_json(self, file_path):
        with open(file_path, "r") as f:
            self.meals_list = json.load(f)

    # 食材データを収集
    # 重複を削除
    def arrange_ingredients(self, file_path):
        self.__read_json(file_path)
        ingredients_list = []
        for meal in self.meals_list:
            ingredients_list.extend(meal["ingredients"])
        ingredients_list = self.__plural_to_singular(ingredients_list)
        # 重複を削除
        ingredients_list = list(set(ingredients_list))
        # アルファベット順にソートする
        ingredients_list = sorted(ingredients_list)
        return ingredients_list
    
    # 単数形＆小文字に変換
    def __plural_to_singular(self, word_list):
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


    def __quickSort(self, array):
        # ベースケース
        if len(array) <= 1:
            return array
        # 再帰的な処理
        else:
            pivot = array[-1]
            lesses = []
            biggers = []
            for i in range(len(array) - 1):
                if array[i] < pivot:
                    lesses.append(array[i])
                else:
                    biggers.append(array[i])
            return self.__quickSort(lesses) + [pivot] + self.__quickSort(biggers)


if __name__ == "__main__":
    dir_current = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    data_operator = DataOperator()
    ingredients_list = data_operator.arrange_ingredients(f"{dir_current}/dir_meal_information/meals.json")
    db_op = db_operator.DbOperator(f"{dir_current}/dir_meal_information/recipie.db")
    db_op.register_ingredients(ingredients_list)
    