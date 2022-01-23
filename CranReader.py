import codecs
import numpy as np

class CranReader:
    def __init__(self, path, mode):
        """
        """
        self.path = path
        self.mode = mode

    def read_text(self):
        txts = []
        with codecs.open(self.path, 'r', 'utf-8') as f:
            line = f.readline()
            while len(line.strip()) > 0:
                if line.strip() == ".W":
                    temp = []
                    line = f.readline()
                    while (not line.strip().find(".I")) or line.strip() != ".T" and len(line.strip()) != 0:
                        temp.append(line.strip())
                        line = f.readline()
                    txts.append(temp)
                line = f.readline()

        self.txts = np.array(txts, dtype=list)
        print(txts)

    def read(self):
        if self.mode == "read_query":
            self.read_query()
        elif self.mode == "read_all":
            self.read_all()
        elif self.mode == "read_text":
            self.read_text()
        else:
            print("There is no such mode")


