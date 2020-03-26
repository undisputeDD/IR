import re
import sys
import time
from MatInc_InvInd.src.File import Files
from MatInc_InvInd.src.Dict import Dict


def make_matrix(dictionary, files):
    all_ids = files.get_ids()
    for word in dictionary.dict:
        new_list = []
        pres_ids = dictionary.get_word_fileids(word)
        current = 0
        for id in all_ids:
            if (current == len(pres_ids)) or (id < pres_ids[current]):
                new_list.append(0)
            elif id == pres_ids[current]:
                new_list.append(id)
                current += 1
            else:
                current += 1
        dictionary.set_word_fileids(word, new_list)

    return dictionary


def making_dictionary():
    start_time = time.time()

    all_words = 0
    fileID = 1
    dictionary = Dict()
    files = Files()
    pattern = re.compile("(?<=[> \n\t])*([a-z0-9][a-z0-9']*-?[a-z0-9][a-z0-9']+)(?=[< \n\t])*")
    for i in range(1, len(sys.argv)):
        print(sys.argv[i])
        with open(sys.argv[i]) as f_reader:
            files.add_file(fileID, f_reader)
            data = f_reader.read().lower()
            find = re.findall(pattern, data)
            all_words += len(find)
            for word in find:
                dictionary.add_word(word)
                dictionary.add_file(word, fileID)
        fileID += 1

    unique_words = len(dictionary.dict.keys())

    '''This creates incidence matrix out of inverted index'''
    #dictionary = make_matrix(dictionary, files)

    f_writer = open('../result/output.txt', 'w')
    f_writer.write(dictionary.to_str())

    print('Quantity of words: ' + str(all_words))
    print('Quantity of unique words: ' + str(unique_words))

    f_writer.close()

    print('Time: ' + str(time.time() - start_time))

    return dictionary


if __name__ == '__main__':
    making_dictionary()
