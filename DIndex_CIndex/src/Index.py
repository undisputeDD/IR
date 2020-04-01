from DIndex_CIndex.src.File import File


class Index:
    def __init__(self):
        self.dict = {}

    def add_word(self, word, fileID, coord):
        if word not in self.dict:
            self.dict[word] = {}
            self.dict[word][fileID] = File(fileID)
            self.dict[word][fileID].add_coord(coord)
        else:
            if fileID not in self.dict[word]:
                self.dict[word][fileID] = File(fileID)
                self.dict[word][fileID].add_coord(coord)
            else:
                self.dict[word][fileID].add_coord(coord)

    def get_word_fileids(self, word):
        return set(self.dict[word].keys())

    def get_word_fileid_coords(self, word, fileID):
        return self.dict[word][fileID].coord

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
                result += '('
                j = 0
                coords = rem_list[elem].coord
                for fid in coords:
                    result += str(fid)
                    if j != len(coords) - 1:
                        result += ', '
                    j += 1
                result += ')'
                if i != len(rem_list) - 1:
                    result += ', '
                i += 1
            result += ']\n'

        return result
