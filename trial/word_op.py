
import pickle
import os
from gensim.models import KeyedVectors
# 前回の実験の結果から、学習済みモデルはpickleで保存しても、
# そんなに読み込みが遅くならないと分かったので、そうする。

dir_current = os.path.dirname(__file__)
path_word = dir_current + '/dir_word/entity_vector.model.bin'

class WordVector:
    def __init__(self):
        self.model = KeyedVectors.load_word2vec_format(path_word, binary=True)

    def find_similarity(self, word):
        return self.model.most_similar(word)



if __name__ == "__main__":
    word_vec = WordVector()
    print(word_vec.find_similarity("オムライス"))
