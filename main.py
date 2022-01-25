import CranReader as CR
import Preprocessing as PR
import VectorSpaceModel as VSM

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


    # Creating Vector Space Model with preprocessed corpus
    vsm = VSM.VectorSpaceModel(p.clean_corpus)
    vsm.calculate_inverted_index()

    # Querying with VSM
    query_index = 8
    related_docs_indices = vsm.calculate_cos_similarity(p_qrs.clean_corpus[query_index - 1])
    print("Clean   query = ", p_qrs.clean_corpus[query_index - 1])
    print("Initial query = ", qrs.txts[query_index - 1])
    print("")
    print("")
    for i in related_docs_indices[:3]:
        data = [rd.txts[i]]
        print(data)
        print(i+1)














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
