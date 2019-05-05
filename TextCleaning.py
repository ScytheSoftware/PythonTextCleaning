import os
import sys
import pandas as pd
import nltk
# nltk.download('all') This line may be needed if you don't have the packages. 
from symspellpy.symspellpy import SymSpell, Verbosity  # import the module
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords


#This function is to make everything lowercase. This isn't needed.
def lowerCase(t): 
	return t.lower()

#A CSV file can be read in by use 'pd.read_csv' but I was getting weird results
#For xls files, install 'xlrd' and maybe 'xls-reader'
data = pd.read_excel("output.xls") #Reading from a file text
 
rawCorpus = data['text'] 

 #The program takes a while. The more data, the longer it takes. This line is here to show the user the program is working.
print("Loading")

Corpus= []
for sentences in range(len(rawCorpus)):
	Corpus.append(lowerCase(str(rawCorpus[sentences])))



maxEditDistanceDictionary = 2 # maximum edit distance per dictionary precalculation
prefix_length = 7

# create object
sym_spell = SymSpell(maxEditDistanceDictionary, prefix_length)

# load dictionary
dictionary_path = "Dictionary.txt"

#I have 'term_index' and 'count_index' here for the purpose of sym_spell, but I do not use them for output data in the program.
term_index = 0  # column of the term in the dictionary text file
count_index = 1  # column of the term frequency in the dictionary text file

if not sym_spell.load_dictionary(dictionary_path, term_index, count_index): #loading the dictionary
	print("Dictionary file not found")


placeHolderList=[]

#lookup suggestions for multi-word input strings 
#Conversion is needed. The sym spell lookup-compound takes string
input_corpus = (str(Corpus))


# max edit distance per lookup (per single word, not per whole input string)
max_edit_distance_lookup = 2
suggestions = sym_spell.lookup_compound(input_corpus,
										max_edit_distance_lookup)
#Putting everything back in a list format. 'PlaceHolderList' is temporary
for suggestion in suggestions:
	placeHolderList.append(suggestion.term) 


stopWords = set(stopwords.words('english')) #getting stop wards to clean up the corpus
#Tokenize made everything separate in a list. Using the 'join' function will makes it a string again.
words = word_tokenize(''.join(placeHolderList)) 


print(words) #Checking the full list

cleanedCorpus = []

#This loop takes out all the stopwords. I didn't add any additional stopwords.
for w in words:
    if w not in stopWords:
        cleanedCorpus.append(w)

print(cleanedCorpus) #outputing the full cleaned list

