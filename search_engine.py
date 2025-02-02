import json, os
import data_operator, synonym_op
from trial import multiple_to_single
import image_operator


def read_datadictionary():
    dir_current = os.path.dirname(os.path.abspath(__file__))
    with open(dir_current + "/dir_word/data.json", "r") as f:
        data_dictionary = json.load(f)
    return data_dictionary

# レシピデータ読取り
recipe_database = read_datadictionary()


def suggest_recipes(ingredients_user):
    # 入力された食材を正規化する
    # ingredients_user = [synonym_operator.getSynonym(ingredient) for ingredient in ingredients_user]
    # ingredients_user = convert_datas_to_singular(ingredients
    ingredients_user = multiple_to_single.plural_to_singular(ingredients_user)

    # 入力された食材から料理を提案する
    suggestions = []
    for recipe_name, recipe_ingredients in recipe_database.items():
        # 材料が全て揃っているかどうかを確認
        result_check = True
        for recipe_ingredient in recipe_ingredients:
            if recipe_ingredient in ingredients_user:
                pass
            else:
                result_check = False
                break
        if result_check:
            dict = {}
            dict["recipe_name"] = recipe_name
            url_image = image_operator.get_image_urls(recipe_name)
            dict["url_image"] = url_image
            suggestions.append(dict)
    # 材料が全て揃っているかどうかを確認
    return suggestions

if __name__ == "__main__":
    user_ingredients = ["Eggs", "Chicken Breast", "Onion", "Rice", "Ketchup", "Pork Loin", "Bread Crumbs", "Flour", "Oil"]

    suggestions = suggest_recipes(user_ingredients)
    print(suggestions)


'''
〇結論
以下が課題と確認した
1.材料名の表記ゆれ
玉ねぎとたまねぎ、鶏むね肉と鶏胸肉など、同じ材料でも表記が異なることがある
→ツール側で表記ゆれを吸収する処理が必要
2.材料の量や調理法の考慮
材料が揃っていても、料理を作るための量や調理法が異なることがある
3.材料の組み合わせの考慮
材料が揃っていても、料理の組み合わせが適切でないことがある

4.入力方法の改善
手打ちで材料を一つ一つ入力するのは手間がかかる。
→入力の手間を少なくする方法を検討したい

'''