import os, sys, string, codecs
import CranReader as CR
import Preprocessing as PR

if __name__ == '__main__':
    print("Read files ")
    rd = CR.CranReader('./CRANFIELD/cran.all.1400', "read_text")
    rd.read()
    
    p = PR.Preprocessing(rd.txts)
    p.tokenize()
    p.remove_stopwords()
    p.word_stemmer()
    
    print(p.stem_tokens)
    


