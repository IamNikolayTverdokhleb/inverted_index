import nltk
from nltk.corpus import stopwords
import re


class Preprocessing:
    """
    This class provides some methods to preprocess text data
    """
    def __init__(self, corpus):
        self.corpus = corpus
        self.number_of_documents = len(corpus)

    def download_stopwords(self):
        """
        This method download stopwords to the system.
        Should be executed once.
        """
        nltk.download('stopwords')

    def tokenize(self):
        """
        This method performs tokenization of the text, i.e. it
        creates a vector of list of tokens (words) per document.
        The length of the array is equal to the number of documents
        in the corpus, and each element of the array is a list with
        all the words presented in each element of the corpus
        """
        self.tokens = []
        for text in self.corpus:
            text = re.sub('[^A-Za-z]+', ' ', text)
            self.tokens.append(nltk.word_tokenize(text))

    def remove_stopwords(self):
        """
        This method removes stopwords (useless words)
        from token array
        """
        stop_words = set(stopwords.words('english'))
        self.clean_tokens = [[word for word in token if word not in stop_words] for token in self.tokens]

    def word_stemmer(self):
        """
        This method performs stemming (normalization)
        of tokens, i.e. it returns the "roots" of each token
        """
        ps = nltk.stem.PorterStemmer()
        self.stem_clean_tokens = []
        for token in self.clean_tokens:
            temp = []
            for words in token:
                temp.append(ps.stem(words))
            self.stem_clean_tokens.append(temp)

    def set_clean_corpus_from_clean_tokens(self):
        """
        This method creates a corpus (array of strings)
        from stemmed cleaned tokens
        """
        self.clean_corpus = []
        for token in self.stem_clean_tokens:
            self.clean_corpus.append(' '.join(token))

    def perform_preprocessing(self):
        """
        This method is a wrapper around all preprocessing routines
        """
        self.tokenize()
        self.remove_stopwords()
        self.word_stemmer()
        self.set_clean_corpus_from_clean_tokens()
