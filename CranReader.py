import codecs


class CranReader:
    """
    This class provides some methods to read data
    from CRANFIELD dataset.
    """
    def __init__(self, path, mode):
        self.path = path # path to the CRANFIELD file
        self.mode = mode #read_query, read_text or read_all

    def read(self):
        """
        This is a wrapper method around
        the reading functions depending on the mode
        """
        if self.mode == "read_query":
            self.read_query()
        elif self.mode == "read_all":
            self.read_all()
        elif self.mode == "read_text":
            self.read_text()
        else:
            print("There is no such mode")

    def read_text(self):
        """
        This method reads all the text documents from CRANFIELD file,
        i.e. all the lines in between ".W" and ".I" tags.
        It writes them to self.txts, which is an array of strings,
        and the length is equal to the number of documents in the file.
        """
        self.txts = []
        with codecs.open(self.path, 'r', 'utf-8') as f:
            line = f.readline()
            while len(line.strip()) > 0:
                if line.strip() == ".W":
                    temp = []
                    line = f.readline()
                    while True:
                        if (line.find(".I") == -1) and len(line.strip()) != 0:
                            temp.append(line.strip())
                            line = f.readline()
                        else:
                            break
                    self.txts.append(str(' '.join(temp)))
                line = f.readline()

