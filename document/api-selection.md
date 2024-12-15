## **APIの候補**

Food APIs

[world.openfoodfacts.org/data](https://world.openfoodfacts.org/data)

Best Food API Solutions for Nutrition and Recipe

[11 Best Food API Solutions for Nutrition and Recipe](https://geekflare.com/dev/food-api-solutions/)

楽天API

[Pythonで楽天レシピAPIからレシピを取得する #Python - Qiita](https://qiita.com/run1000dori/items/7ffa7907a6c03c8909fc)

## 観点

1.無料で使える

2.表記ゆれの心配が少ない

3.料理名の一覧取得が出来る。レシピの情報の取得が出来る

## 比較

| 評価指標               | Food APIs | the MealDB | 楽天API |
| ---------------------- | --------- | ---------- | ------- |
| 料理名一覧取得         | ×        | 〇         | 〇      |
| レシピ取得             | 〇        | ◎         | 〇      |
| 無料で使える           | 〇        | 〇         | 〇      |
| 表記ゆれの心配なし     | 〇        | 〇         | △      |
| 料理の写真が取得できる | ×        | 〇         | △      |

取得が確認できたもの

* 楽天API: 表記ゆれや書きっぷりの無法っぷりがひどい
* Food APIs: 好きに情報とれるかが謎

## 結論

TheMealDBのAPIで実現する

[Free Meal API | TheMealDB.com](https://www.themealdb.com/api.php)

## やりたいこと

1. 料理一覧の情報を取得
2. 材料の情報を取得
3. レシピの情報を取得
4. 料理の画像

1→a→z

2→1の結果の"strIngredient＊"を取得

3→strInstructions

4→strMealThumb
