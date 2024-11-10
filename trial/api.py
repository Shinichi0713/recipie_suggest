import requests

# APIエンドポイント
api_url = "https://example.com/api/food_synonyms"

# 食材の類義語を取得する関数
def get_food_synonyms(food_name):
    response = requests.get(f"{api_url}?query={food_name}")
    if response.status_code == 200:
        return response.json()
    else:
        return None

# 例: "apple"の類義語を取得
synonyms = get_food_synonyms("リンゴ")
if synonyms:
    print("類義語:", synonyms)
else:
    print("データを取得できませんでした")