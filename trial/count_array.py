# 配列Aと配列Bを定義
A = [1, 2, 3, 4, 5]
B = [4, 5, 6, 7, 8]

# AとBの共通部分を見つける
intersection = set(A) & set(B)

# 共通部分の要素数をカウント
count = len(intersection)

print(f"配列Aと配列Bの重複する要素数は {count} です。")