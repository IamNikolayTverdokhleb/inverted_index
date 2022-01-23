import os, sys, string, codecs
import CranReader as CR

if __name__ == '__main__':
    print("Read files ")
    rd = CR.CranReader('./CRANFIELD/cran.all.1400', "read_text")
    rd.read()
    rd.tokenize()
    rd.word_stemmer()
    rd.remove_stopwords()

