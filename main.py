import os, sys, string, codecs
from CranReader import *

if __name__ == '__main__':
    print("Read files ")
    rd = CranReader('./CRANFIELD/cran.all.1400', "read_text")
    rd.read()

