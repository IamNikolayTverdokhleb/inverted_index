import codecs
import numpy as np
import nltk
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
import re
import pandas as pd

class Preprocessing:
    def __init__(self, file):
        self.file = file
        self.number_of_documents = len(file)

    def tokenize(self):
        self.tokens = []
        for text in self.file:
            text = re.sub('[^A-Za-z]+', ' ', text)
            self.tokens.append(nltk.word_tokenize(text))

    def remove_stopwords(self):
        stop_words = set(stopwords.words('english'))
        self.clean_tokens = [[word for word in token if word not in stop_words] for token in self.tokens]

    def word_stemmer(self):
        ps = nltk.stem.PorterStemmer()
        self.stem_clean_tokens = []
        for token in self.clean_tokens:
            temp = []
            for words in token:
                temp.append(ps.stem(words))
            self.stem_clean_tokens.append(temp)

    def vectorizer(self):
        clean_corpus = []
        for token in self.stem_clean_tokens:
            clean_corpus.append(' '.join(token))
        vectorizerX = TfidfVectorizer()
        vectorizerX.fit(clean_corpus)
        doc_vector = vectorizerX.transform(clean_corpus)
        # print(vectorizerX.get_feature_names())
        #
        # print(doc_vector.shape)
        df1 = pd.DataFrame(doc_vector.toarray(), columns=vectorizerX.get_feature_names())
        print(df1)