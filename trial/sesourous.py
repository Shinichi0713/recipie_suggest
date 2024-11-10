from nltk.corpus import wordnet
import nltk
nltk.download("wordnet")

synsets = wordnet.synsets("米",lang='jpn')
for syn in synsets:
    print(syn,":",syn.definition())

rice_synset=synsets[0]
synonyms=rice_synset.lemma_names("jpn")
print(synonyms)