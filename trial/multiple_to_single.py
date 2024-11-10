import inflect
import json, os

# 食材とそれを使った料理のデータベース（辞書）
recipe_database = {
    "Omelette Rice": ["Eggs", "Chicken Breast", "Onion", "Rice", "Ketchup"],
    "Curry Rice": ["Meat", "Potatoes", "Carrots", "Onion", "Curry Roux"],
    "Ramen": ["Chinese Noodles", "Pork", "Bean Sprouts", "Green Onions", "Ramen Soup"],
    "Sushi": ["Fish", "Sushi Rice", "Seaweed", "Vinegar", "Sugar", "Salt"],
    "Tempura": ["Shrimp", "Sweet Potato", "Eggplant", "Pumpkin", "Tempura Batter", "Oil"],
    "Udon": ["Udon Noodles", "Dashi", "Soy Sauce", "Green Onions", "Bonito Flakes"],
    "Soba": ["Soba Noodles", "Dashi", "Soy Sauce", "Green Onions", "Wasabi"],
    "Takoyaki": ["Octopus", "Takoyaki Batter", "Dashi", "Cabbage", "Tempura Bits", "Sauce"],
    "Okonomiyaki": ["Okonomiyaki Batter", "Dashi", "Cabbage", "Pork", "Sauce"],
    "Yakisoba": ["Chinese Noodles", "Pork", "Cabbage", "Bean Sprouts", "Green Peppers", "Sauce"],
    "Gyoza": ["Pork", "Cabbage", "Garlic Chives", "Garlic", "Gyoza Wrappers"],
    "Sukiyaki": ["Beef", "Tofu", "Chinese Cabbage", "Shiitake Mushrooms", "Sukiyaki Sauce"],
    "Shabu-shabu": ["Pork", "Chinese Cabbage", "Enoki Mushrooms", "Shimeji Mushrooms", "Dashi"],
    "Tonkatsu": ["Pork Loin", "Bread Crumbs", "Eggs", "Flour", "Oil"],
    "Karaage": ["Chicken Thigh", "Soy Sauce", "Garlic", "Ginger", "Flour", "Oil"],
    "Nikujaga": ["Beef", "Potatoes", "Carrots", "Onion", "Soy Sauce", "Sugar", "Mirin"],
    "Mapo Tofu": ["Tofu", "Ground Meat", "Garlic Chives", "Doubanjiang", "Soy Sauce", "Sake", "Sugar"],
    "Hiyashi Chuka": ["Chinese Noodles", "Cucumber", "Ham", "Tomato", "Hiyashi Chuka Sauce"],
    "Beef Stew": ["Beef", "Potatoes", "Carrots", "Onion", "Red Wine", "Canned Tomatoes", "Butter"],
    "Hamburger Steak": ["Ground Meat", "Bread Crumbs", "Milk", "Onion", "Eggs", "Sauce"],
    # Other ingredients and dishes can be added
}


def plural_to_singular(word_list):
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


def convert_datas_to_singular(ingredients):
    # 辞書型データを呼び出す
    for key, content in recipe_database.items():
        # 単数形に変換
        print(content)
        singulars = plural_to_singular(content)
        ingredients[key] = singulars
    return ingredients
    



if __name__ == "__main__":

    # # 例の単語リスト
    # words = ["Eggs", "Potatoes", "Carrots", "Onions", "Green Onions", "Shrimp", "Sweet Potatoes", "Eggplants", "Pumpkins", "Tempura Bits"]

    # # 単数形に変換
    # singular_words = plural_to_singular(words)
    # print(singular_words)
    recipe_database = convert_datas_to_singular(recipe_database)
    dir_current = os.path.dirname(os.path.abspath(__file__))

    with open(dir_current + '/data.json', 'w') as json_file:
        json.dump(recipe_database, json_file, indent=4)