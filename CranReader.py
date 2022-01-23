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
            while line:
                if line.strip() == ".W":
                    temp = []
                    while (not line.strip().find(".I")) or line.strip() != ".T" or line:
                        print("While not Line ", line)
                        temp.append(line.strip())
                        line = f.readline()
                    print("TEMP = ", temp)
                    txts.append(temp)
                line = f.readline()

        txts = np.array(txts)
        print(txts.shape)
        print(txts)
        print(len(txts))

    def read(self):
        if self.mode == "read_query":
            self.read_query()
        elif self.mode == "read_all":
            self.read_all()
        elif self.mode == "read_text":
            self.read_text()
        else:
            print("There is no such mode")


