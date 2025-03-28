from flask import Flask, render_template, request, jsonify, redirect, url_for
import os, csv

os.chdir(os.path.dirname(__file__))
app = Flask(__name__)

import search_engine

ingredients_input = []
items = {}
items_selectable = []
selected_category = None

@app.route('/', methods=['GET', 'POST'])
def index():
    global items_selectable, selected_category
    suggestions = None
    candidates = None
    if request.method == "POST":
        if 'category'in request.form:
            selected_category = request.form['category']
            items_selectable = items[selected_category]
            print(selected_category)
        if 'item_selected' in request.form:
            item_selected = request.form.get('item_selected')
            if item_selected not in ingredients_input:
                ingredients_input.append(item_selected)
        if 'search' in request.form:
            print(ingredients_input)
            # 検索処理
            suggestions, candidates = search_engine.suggest_recipes(ingredients_input)
            print(suggestions)
            print(candidates)
    return render_template('index.html', ingredients=ingredients_input, items_selectable=items_selectable, result = suggestions, categories=items.keys(), selected_category=selected_category, candidates=candidates)

@app.route('/remove_ingredient/<ingredient>', methods=['DELETE'])
def remove_ingredient(ingredient):
    try:
        ingredients_input.remove(ingredient)
        print(ingredients_input)
        return jsonify(success=True), 200
    except ValueError:
        return jsonify(success=False), 404

def read_ingredients():
    dir_current = os.path.dirname(__file__)
    with open(dir_current + '/dir_word/ingredients_category.csv', 'r') as fp:
        reader = csv.DictReader(fp)
        for row in reader:
            category = row["ジャンル"]
            item = row["食材"]
            if category not in items:
                items[category] = []
            items[category].append(item)
    return items


if __name__ == "__main__":
    read_ingredients()
    app.run(debug=True)
