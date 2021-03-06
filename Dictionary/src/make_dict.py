import re
import sys
import json
import time


def making_dictionary():
    start_time = time.time()

    all_words = 0
    dictionary = {}
    pattern = re.compile("(?<=[> \n\t])*([a-z0-9][a-z0-9']*-?[a-z0-9][a-z0-9']+)(?=[< \n\t])*")
    for i in range(1, len(sys.argv)):
        print(sys.argv[i])
        with open(sys.argv[i]) as f_reader:
            data = f_reader.read().lower()
            find = re.findall(pattern, data)
            all_words += len(find)
            for word in find:
                try:
                    dictionary[word]
                except KeyError:
                    dictionary[word] = 0

    unique_words = len(dictionary.keys())
    dictionary = sorted(dictionary.keys())

    f_writer = open('../result/output.json', 'w')
    json.dump(dictionary, f_writer)

    print('Quantity of words: ' + str(all_words))
    print('Quantity of unique words: ' + str(unique_words))

    f_writer.close()

    print('Time: ' + str(time.time() - start_time))


if __name__ == '__main__':
    making_dictionary()
