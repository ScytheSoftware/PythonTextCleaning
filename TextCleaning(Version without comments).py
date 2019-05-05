#Version without comments

import os
import sys
import pandas as pd
import nltk
from symspellpy.symspellpy import SymSpell, Verbosity 
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords


def lowerCase(t): 
	return t.lower()

data = pd.read_excel("output.xls") 
rawCorpus = data['text'] 

print("Loading")

Corpus= []
for sentences in range(len(rawCorpus)):
	Corpus.append(lowerCase(str(rawCorpus[sentences])))

#-------
maxEditDistanceDictionary = 2
prefix_length = 7
sym_spell = SymSpell(maxEditDistanceDictionary, prefix_length)

dictionary_path = "Dictionary.txt"

term_index = 0 
count_index = 1 

if not sym_spell.load_dictionary(dictionary_path, term_index, count_index): #loading the dictionary
	print("Dictionary file not found")
#-------


placeHolderList=[]
input_corpus = (str(Corpus))
max_edit_distance_lookup = 2
suggestions = sym_spell.lookup_compound(input_corpus,
										max_edit_distance_lookup)
for suggestion in suggestions:
	placeHolderList.append(suggestion.term) 

#-------
stopWords = set(stopwords.words('english')) 
words = word_tokenize(''.join(placeHolderList)) 


print(words)


cleanedCorpus = []
for w in words:
    if w not in stopWords:
        cleanedCorpus.append(w)

print(cleanedCorpus)

