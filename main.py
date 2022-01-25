import CranReader as CR
import Preprocessing as PR
import VectorSpaceModel as VSM
import LanguageModel as LM

if __name__ == '__main__':
    # Reading corpus
    rd = CR.CranReader('./CRANFIELD/cran.all.1400', "read_text")
    rd.read()

    # Preprocessing corpus
    p = PR.Preprocessing(rd.txts)
    p.perform_preprocessing()

    # Reading queris
    qrs = CR.CranReader('./CRANFIELD/cran.qry', "read_text")
    qrs.read()
    # Preprocessing queris
    p_qrs = PR.Preprocessing(qrs.txts)
    p_qrs.perform_preprocessing()

    # Choosing query
    query_index = 8
    print("Clean   query = ", p_qrs.clean_corpus[query_index - 1])
    print("Initial query = ", qrs.txts[query_index - 1])


    # Creating Vector Space Model with preprocessed corpus
    print("Creating Vector Space Model with preprocessed corpus")
    vsm = VSM.VectorSpaceModel(p.clean_corpus)
    vsm.calculate_inverted_index()

    # Querying with VSM
    related_docs_indices_vsm = vsm.calculate_cos_similarity(p_qrs.clean_corpus[query_index - 1])

    # Printing 3 of the best matches for VSM
    for i in related_docs_indices_vsm[:3]:
        data = [rd.txts[i]]
        print(data)

    # Creating Language Model with preprocessed corpus
    print("Creating Language Model with preprocessed corpus")
    lm = LM.LanguageModel(p.stem_clean_tokens, p.clean_corpus)
    lm.calculate_TF_IDF()
    related_docs_indices_lm = lm.query_likelihood(p_qrs.stem_clean_tokens[query_index - 1])

    # Printing 3 of the best matches for LM with query likelyhood
    for i in related_docs_indices_lm[:3]:
        data = [rd.txts[i]]
        print(data)













if __name__ == '__test_main__':
    test_corpus = [
        'In computer science artificial intelligence sometimes called machine intelligence is intelligence demonstrated by machines',

        'Experimentation calculation and Observation is called science',

        'Physics is a natural science that involves the study of matter and its motion through space and time, along with related concepts such as energy and force',

        'In mathematics and computer science an algorithm is a finite sequence of well-defined computer-implementable instructions',

        'Chemistry is the scientific discipline involved with elements and compounds composed of atoms, molecules and ions',

        'Biochemistry is the branch of science that explores the chemical processes within and related to living organisms',

        'Sociology is the study of society, patterns of social relationships, social interaction, and culture that surrounds everyday life',
    ]

    test_query = ['computer science']

    # Preprocessing corpus
    p = PR.Preprocessing(test_corpus)
    p.perform_preprocessing()

    # Creating Vector Space Model with preprocessed corpus
    vsm = VSM.VectorSpaceModel(p.clean_corpus)
    vsm.vectorizer()

    # Reading queris
    p_qrs = PR.Preprocessing(test_query)
    p_qrs.perform_preprocessing()

    vsm.calculate_cos_similarity(p_qrs.clean_corpus[0])
    print("Clean query = ", p_qrs.clean_corpus[0])
    print("Clean query = ", p_qrs.clean_corpus)
