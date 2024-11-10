# -*- coding: utf-8 -*-
# Wordnet via Python3
# 
# ref:
#   WordList_JP: https://bond-lab.github.io/wnja/
#   python3: http://sucrose.hatenablog.com/entry/20120305/p1
import os, sqlite3
from collections import namedtuple
from pprint import pprint


class SynonymOperator:
    def __init__(self) -> None:
        self.dir_current = os.path.dirname(os.path.abspath(__file__))
        self.conn = sqlite3.connect(self.dir_current + "/dir_word/wnjpn.db")
        self.Word = namedtuple('Word', 'wordid lang lemma pron pos')
        self.Sense = namedtuple('Sense', 'synset wordid lang rank lexid freq src')
        self.Synset = namedtuple('Synset', 'synset pos name src')

    def getWords(self, lemma):
        cur = self.conn.execute("select * from word where lemma=?", (lemma,))
        return [self.Word(*row) for row in cur]

    def getSenses(self, word):
        cur = self.conn.execute("select * from sense where wordid=?", (word.wordid,))
        return [self.Sense(*row) for row in cur]

    def getSynset(self, synset):
        cur = self.conn.execute("select * from synset where synset=?", (synset,))
        return self.Synset(*cur.fetchone())

    def getWordsFromSynset(self, synset, lang):
        cur = self.conn.execute("select word.* from sense, word where synset=? and word.lang=? and sense.wordid = word.wordid;", (synset,lang))
        return [self.Word(*row) for row in cur]

    def getWordsFromSenses(self, sense, lang="jpn"):
        synonym = {}
        for s in sense:
            lemmas = []
            syns = self.getWordsFromSynset(s.synset, lang)
            for sy in syns:
                lemmas.append(sy.lemma)
                synonym[self.getSynset(s.synset).name] = lemmas
        return synonym


    # 類似語取得
    def getSynonym (self, word):
        synonym = {}
        words = self.getWords(word)
        if words:
            for w in words:
                sense = self.getSenses(w)
                s = self.getWordsFromSenses(sense)
                synonym = dict(list(synonym.items()) + list(s.items()))
        if len(synonym) == 0:
            print(f"Word {word} is not found in the database")
            return word
        else:
            key_priority = list(synonym.keys())[0]
        represent_synonym = synonym[key_priority][0]
        return represent_synonym




if __name__ == '__main__':
    synonym_op = SynonymOperator()
    synonym = synonym_op.getSynonym("たまねぎ")
    pprint(synonym)