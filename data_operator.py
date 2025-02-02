
import os, json
import pandas as pd
import synonym_op
from googletrans import Translator


# dbからデータを取得・操作するクラス
class DataOperator:
    def __init__(self):
        self.data = []
        self.dir_current = os.path.dirname(os.path.abspath(__file__))
        self.path_data = self.dir_current + "/dir_word/data.json"
        self.__load_data()


    def __load_data(self):
        with open(self.path_data, 'r', encoding='utf-8') as fp:
            self.data = json.load(fp)

    def get_data(self):
        return self.data


    def write_data(self, data):
        with open(self.path_data, 'w', encoding='utf-8') as fp:
            json.dump(data, fp, ensure_ascii=False, indent=4)
        print("Data has been written.")

    def refine_data(self):
        synonym_operator = synonym_op.SynonymOperator()
        for key, value in self.data.items():
            for i, ingredient in enumerate(value):
                synonym = synonym_operator.getSynonym(ingredient)
                self.data[key][i] = synonym

    def convert_to_csv(self):
        ingredients_registered = []
        for key, value in self.data.items():
            for ingredient in value:
                if ingredient not in ingredients_registered:
                    ingredients_registered.append(ingredient)
        dir_current = os.path.dirname(os.path.abspath(__file__))
        df = pd.DataFrame(ingredients_registered)
        df.to_csv(dir_current + '/ingredients_used.csv', index=False)

def translate_en_to_ja(text):
    translator = Translator()
    result = translator.translate(text, src='ja', dest='en')
    return result.text.lower() 

if __name__ == "__main__":
    data_operator = DataOperator()
    data_operator.convert_to_csv()
    
    