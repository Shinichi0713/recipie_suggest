
import os
import sqlite3


class DbOperator():
    def __init__(self, db_path):
        self.db_path = db_path
        if os.path.exists(db_path):
            print("database connect")
            self.conn = sqlite3.connect(db_path)
            self.cursor = self.conn.cursor()

            sql_str = "SELECT name FROM sqlite_master WHERE type = 'table';"
            self.cursor.execute(sql_str)
            tables = self.cursor.fetchall()
            print(tables)
        else:
            raise FileNotFoundError(f"Database not found at {db_path}")

    # 食材をDBに登録する
    def register_ingredients(self, ingeredients_list):
        sql_str = "INSERT INTO Ingredients (ingredients, gentre) VALUES (?, ?)"
        for ingredient in ingeredients_list:
            self.cursor.execute(sql_str, (ingredient, ""))
        self.conn.commit()


    def __del__(self):
        self.conn.close()




if __name__ == "__main__":
    dir_current = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    db = DbOperator(f"{dir_current}/dir_meal_information/recipie.db")
    print(db.db_path)


