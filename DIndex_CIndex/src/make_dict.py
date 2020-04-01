import re
import sys
import time
from DIndex_CIndex.src.File import Files
from DIndex_CIndex.src.Dict import Dict
from DIndex_CIndex.src.Index import Index


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
    pattern = re.compile("(?<=[> \n\t])*([a-z0-9][a-z0-9']*-?[a-z0-9][a-z0-9']*)(?=[< \n\t])*")
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

    print('Quantity of words: ' + str(all_words))
    print('Quantity of unique words: ' + str(unique_words))
    print('Time: ' + str(time.time() - start_time))

    return dictionary, files


def making_d_index():
    start_time = time.time()

    all_pairs = 0
    fileID = 1
    dictionary = Dict()
    files = Files()
    pattern = re.compile("(?<=[> \n\t])*([a-z0-9][a-z0-9']*-?[a-z0-9][a-z0-9']*)(?=[< \n\t])*")
    for i in range(1, len(sys.argv)):
        print(sys.argv[i])
        with open(sys.argv[i]) as f_reader:
            files.add_file(fileID, f_reader)
            data = f_reader.read().lower()
            find = re.findall(pattern, data)
            all_pairs += len(find) - 1
            for i in range(0, len(find) - 1):
                word = find[i] + ' ' + find[i + 1]
                dictionary.add_word(word)
                dictionary.add_file(word, fileID)
        fileID += 1

    unique_pairs = len(dictionary.dict.keys())

    print('Quantity of pairs: ' + str(all_pairs))
    print('Quantity of unique pairs: ' + str(unique_pairs))
    print('Time: ' + str(time.time() - start_time))

    return dictionary, files


def making_c_index():
    start_time = time.time()

    all_words = 0
    fileID = 1
    index = Index()
    files = Files()
    pattern = re.compile("(?<=[> \n\t])*([a-z0-9][a-z0-9']*-?[a-z0-9][a-z0-9']*)(?=[< \n\t])*")
    for i in range(1, len(sys.argv)):
        print(sys.argv[i])
        with open(sys.argv[i]) as f_reader:
            files.add_file(fileID, f_reader)
            data = f_reader.read().lower()
            find = re.findall(pattern, data)
            all_words += len(find)
            i = 1
            for word in find:
                index.add_word(word, fileID, i)
                i += 1
        fileID += 1

    unique_words = len(index.dict.keys())

    print('Quantity of words: ' + str(all_words))
    print('Quantity of unique words: ' + str(unique_words))
    print('Time: ' + str(time.time() - start_time))

    return index, files


if __name__ == '__main__':
    dictionary = making_dictionary()

    f_writer = open('../result/output.txt', 'w')
    f_writer.write(dictionary.to_str())
    f_writer.close()
