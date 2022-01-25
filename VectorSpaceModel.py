from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd


class VectorSpaceModel:
    """
    This class implements Vector Space Model for text representation
    and quering.
    """

    def __init__(self, corpus):
        self.corpus = corpus

    def write_inverted_file(self, path, mode="Pandas_CSV"):
        """
        This method writes inverted file to the disk to speed up the search later on.
        Only support pandas+CSV combination for now.
        # TODO add more supported formats
        """
        if mode == "Pandas_CSV":
            df1 = pd.DataFrame(self.doc_vector.toarray(), columns=self.vectorizerX.get_feature_names())
            df1.to_csv(path)

    def read_inverted_file(self, path, mode="Pandas_CSV"):
        """
        This method reads inverted file to the memory.
        Only support pandas+CSV combination for now.
        # TODO add more supported formats
        """
        if mode == "Pandas_CSV":
            df1 = pd.read_csv(path)

    def calculate_inverted_index(self, show=False):
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

        # If the user wants to see the table (normally the huge one)
        if show:
            df1 = pd.DataFrame(self.doc_vector.toarray(), columns=self.vectorizerX.get_feature_names())
            print(df1)

    def calculate_cos_similarity(self, clean_query):
        """
        This method calculates cosine similarities between the query
        and the corpus and returns indexes of best matches
        """
        query_vector = self.vectorizerX.transform([clean_query])
        cosineSimilarities = cosine_similarity(self.doc_vector, query_vector).flatten()
        related_docs_indices = cosineSimilarities.argsort()[:-10:-1]
        print(related_docs_indices)

        return related_docs_indices

