import re
import sys
import json
import pickle

all_words = 0
unique_words = 0
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
                unique_words += 1

dictionary = sorted(dictionary.keys())

f_writer = open('../result/output.json', 'w')
json.dump(dictionary, f_writer)
bf_writer = open('../result/output.pickle', 'bw')
pickle.dump(dictionary, bf_writer)

print('Quantity of words: ' + str(all_words))
print('Quantity of unique words: ' + str(unique_words))

f_writer.close()
bf_writer.close()
