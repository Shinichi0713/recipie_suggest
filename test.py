# 食材とそれを使った料理のデータベース（辞書）
recipe_database = {
    "鶏肉": ["チキンカレー", "鶏の唐揚げ", "チキンソテー"],
    "豚肉": ["豚の生姜焼き", "豚肉の味噌煮", "豚肉のガーリックソテー"],
    "牛肉": ["ビーフストロガノフ", "牛肉のすき焼き", "ビーフカレー"],
    "キャベツ": ["キャベツのコールスロー", "キャベツの炒め物", "キャベツのスープ"],
    # 他の食材と料理も追加可能
}

def suggest_recipes(ingredients):
    # 入力された食材から料理を提案する
    suggestions = []
    for ingredient in ingredients:
        if ingredient in recipe_database:
            suggestions.extend(recipe_database[ingredient])
    return suggestions

# ユーザーからの食材の入力
user_ingredients = ["鶏肉", "キャベツ"]

# 料理の提案
suggested_recipes = suggest_recipes(user_ingredients)
print("あなたの食材から作れそうな料理は以下の通りです：")
for recipe in suggested_recipes:
    print(recipe)