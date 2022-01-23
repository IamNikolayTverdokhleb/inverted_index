import codecs
import numpy as np
import nltk
from nltk.corpus import stopwords
import re

# nltk.download('punkt')
# nltk.download('stopwords')

class CranReader:
    def __init__(self, path, mode):
        """
        """
        self.path = path
        self.mode = mode

    def read_text(self):
        self.txts = []
        with codecs.open(self.path, 'r', 'utf-8') as f:
            line = f.readline()
            while len(line.strip()) > 0:
                if line.strip() == ".W":
                    temp = []
                    line = f.readline()
                    while True:
                        if (line.find(".I") == -1) and len(line.strip()) != 0:
                            temp.append(line.strip())
                            line = f.readline()
                        else:
                            break
                    self.txts.append(str(' '.join(temp)))
                line = f.readline()

        # self.txts = str(' '.join(self.txts))

    def read(self):
        if self.mode == "read_query":
            self.read_query()
        elif self.mode == "read_all":
            self.read_all()
        elif self.mode == "read_text":
            self.read_text()
        else:
            print("There is no such mode")

    def tokenize(self):
        self.tokens = []
        for text in self.txts:
            text = re.sub('[^A-Za-z]+', ' ', text)
            self.tokens.append(nltk.word_tokenize(text))

    def word_stemmer(self):
        ps = nltk.stem.PorterStemmer()
        self.stem_tokens = []
        for token in self.tokens:
            temp = []
            for words in token:
                temp.append(ps.stem(words))
            self.stem_tokens.append(temp)

    def remove_stopwords(self):
        stop_words = set(stopwords.words('english'))
        self.clean_stem_tokens = [[word for word in token if word not in stop_words] for token in self.stem_tokens]



