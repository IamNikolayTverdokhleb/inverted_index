import codecs
import numpy as np
import nltk
from nltk.corpus import stopwords
import re

class Preprocessing:
    def __init__(self, file):
        self.file = file
        self.number_of_documents = len(file)

    def tokenize(self):
        self.tokens = []
        for text in self.file:
            text = re.sub('[^A-Za-z]+', ' ', text)
            self.tokens.append(nltk.word_tokenize(text))

    def word_stemmer(self):
        ps = nltk.stem.PorterStemmer()
        self.stem_tokens = []
        for token in self.clean_tokens:
            temp = []
            for words in token:
                temp.append(ps.stem(words))
            self.stem_tokens.append(temp)

    def remove_stopwords(self):
        stop_words = set(stopwords.words('english'))
        self.clean_tokens = [[word for word in token if word not in stop_words] for token in self.tokens]