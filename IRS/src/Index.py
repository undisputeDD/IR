

class Index:

    def __init__(self):
        self.index = {}

    def to_str(self):
        result = ''
        for term in sorted(self.index.keys()):
            result += term
            for i in range(40 - len(term)):
                result += ' '
            result += '['
            j = 0
            key_length = len(self.index[term].post_list.keys())
            for file_id in self.index[term].post_list.keys():
                result += str(file_id)
                result += '('
                i = 0
                coord_length = len(self.index[term].post_list[file_id].coord_list)
                for coord in self.index[term].post_list[file_id].coord_list:
                    result += str(coord)
                    if i != coord_length - 1:
                        result += ', '
                    i += 1
                result += ')'
                if j != key_length - 1:
                    result += ', '
                j += 1
            result += ']\n'
        return result
