from MatInc_InvInd.src.make_dict import making_dictionary
from MatInc_InvInd.src.search import search

dictionary = making_dictionary()
search(dictionary)


f_writer = open('../result/output.txt', 'w')
f_writer.write(dictionary.to_str())
f_writer.close()
