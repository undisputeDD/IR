class Dict:
    def __init__(self):
        self.dict = {}

    def add_word(self, word):
        if word not in self.dict:
            self.dict[word] = set()

    def add_file(self, word, fileID):
        if fileID not in self.dict[word]:
            self.dict[word].add(fileID)

    def get_word_fileids(self, word):
        return self.dict[word]

    def set_word_fileids(self, word, fileids):
        self.dict[word] = fileids

    def to_str(self):
        result = ''
        for word in sorted(self.dict):
            result += word
            for i in range(0, 40 - len(word)):
                result += ' '
            result += '['
            rem_list = self.dict[word]
            i = 0
            for elem in rem_list:
                result += str(elem)
                if i != len(rem_list) - 1:
                    result += ', '
                i += 1
            result += ']\n'

        return result
