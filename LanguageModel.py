from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
import numpy as np

class LanguageModel:
    """
    This class implements Language Model
    with likelyhood query approach
    # TODO: now it's 1-gramm, try other maybe
    """

    def __init__(self, tokens, corpus):
        self.tokens = tokens
        self.corpus = corpus

    def calculate_TF_IDF(self,):
        """
        This method takes the corpus (it's better if it was preprocessed)
        and creates TF-IDF representation of it.
        The table (with pandas) is the following:
                        |   word1   |   word2   | ...
        tf-idf for doc1 | tf-idf_11 | tf-idf_12 | ...
        tf-idf for doc2 | tf-idf_21 | tf-idf_22 | ...
        ...             |   ...     |   ...     | ...
        """
        self.vectorizerX = TfidfVectorizer()
        self.vectorizerX.fit(self.corpus)
        self.doc_vector = self.vectorizerX.transform(self.corpus)

    def query_likelihood(self, query_tokens):
        """
        This method calculates likelyhood of the query and each
        text in the corpus. Note: needs tokenized query
        """

        eps = 0.000001  # To deal with zero-probabilities of terms
        probs = []  # To store p(q|d_i)

        # Transform TF-IDF model to pandas to simplify the following code
        df1 = pd.DataFrame(self.doc_vector.toarray(), columns=self.vectorizerX.get_feature_names())

        # For each text in corpus calculate p(q|d_i)
        for line in range(len(df1)):
            doc_tfidf = df1.loc[line]
            prob = 0
            # For each word in query
            for q in query_tokens:
                prob += np.log(doc_tfidf[q] + eps)
            #  Maybe we have to divide by real len of document instead of len(doc_tfidf) which is constant
            #print("len(self.corpus[line] = ", len(self.corpus[line]))
            #prob /= len(self.corpus[line])
            prob /= len(doc_tfidf)
            probs.append(prob)

        probs_np = np.array(probs)
        related_docs_indices = np.argsort(probs_np)[:-10:-1]
        print("Related docs indices with LM", related_docs_indices)
        return related_docs_indices
