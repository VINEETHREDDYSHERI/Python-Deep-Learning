# packages for web scraping
import requests
from bs4 import BeautifulSoup
import re

# importing the nltk packages that are required for the doing NLP task
import nltk
# Downloading the necessary modules from nltk.
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')
nltk.download('maxent_ne_chunker')
nltk.download('words')
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk import pos_tag
from nltk.stem import PorterStemmer, LancasterStemmer, SnowballStemmer, WordNetLemmatizer
from nltk import ngrams, ne_chunk

html = requests.get("https://en.wikipedia.org/wiki/Google")  # Getting the content of the site
bsObj = BeautifulSoup(html.content, "html.parser")  # Parsing the html data
print("The Title of the page is: ", bsObj.title.string)  # Printing the title of page

# Extracting text from the paragraph tag
paras = []
for paragraph in bsObj.find_all('p'):
    paras.append(str(paragraph.text))

# Extracting text from paragraph header
heads = []
for head in bsObj.find_all('span', attrs={'mw-headline'}):
    heads.append(str(head.text))

# Interleave paragraphs & headers
text = [val for pair in zip(paras, heads) for val in pair]
text = '\n '.join(text)
text = re.sub(r"\[.*?\]+", '', text) # Dropping the footnote superscripts in the brackets

outPutFile = open("input.txt", "w")  # Opening the file in write mode
outPutFile.write(text)  # Writing the content to the file

inPutFile = open("input.txt", "r")  # Opening the input.txt file in read mode
corpus_data = inPutFile.read()  # Reading the data
corpus_data = corpus_data.replace('\n', '')  # Removing the newLine

# Tokenization
# Two variation of tokenization
sen_tokens = sent_tokenize(corpus_data)  # sentence tokenization
word_tokens = word_tokenize(corpus_data)  # word tokenization
print("Sentence Tokens: ")
for idx in range(11):  # Printing the first 10 sentence tokens
    print(sen_tokens[idx])
print("Word Tokens: ")
print(word_tokens[:15])  # Printing the first 15 word tokens

# Part of Speech (POS)
print("POS: ")
partOfSpeech = pos_tag(word_tokens)  # partOfSpeech of every word in the corpus
print(partOfSpeech[:10])  # Printing the first 15 words and its POS

# Stemming converts the given word to its root word by following some predefined conditions.
# It doesn't take context of sentence into consideration.
# Three variation of stemming
print("Stemming: ")
lancasterStem = LancasterStemmer()
porterStem = PorterStemmer()
snowballStem = SnowballStemmer('english')
lancasterStemWords = []
porterStemWords = []
snowballStemWords = []

for word in word_tokens:
    lancasterStemWords.append((word + " -> " + lancasterStem.stem(word)))
    porterStemWords.append((word + " -> " + porterStem.stem(word)))
    snowballStemWords.append((word + " -> " + snowballStem.stem(word)))

# Printing first 10 words and its root word after applying the stemming
print("Lancaster Stemmer")
print(lancasterStemWords[:10])
print("Porter Stemmer")
print(porterStemWords[:10])
print("Snowball Stemmer")
print(porterStemWords[:10])

# Lemmatization on the other hand converts given word to root word by taking the context into consideration
# i.e First find POS and then applies normalization rules to convert the word into root word
# It is slow when compared to stemming
print("WordNet Lemmatization: ")
wordNetLemmatizer = WordNetLemmatizer()
wordNetLemmatizerWord = []
for word in word_tokens:
    wordNetLemmatizerWord.append(
        (word + "->" + wordNetLemmatizer.lemmatize(word)))
print(wordNetLemmatizerWord[:10])

# Trigram
trigrams = ngrams(word_tokens, 3)
count = 1
# Printing the first 10 trigrams
print("Trigrams: ")
for trigram in trigrams:
    print(trigram)
    if count == 10:
        break
    count += 1

# Named Entity Recognition
# It will classifies whether the word is name of person, location, organization etc.
namedEntityRecognition = ne_chunk(pos_tag(word_tokens))
print("Named Entity Recognition: ")
print(namedEntityRecognition[:20])  # Printing the first 20 words in the sentence.
