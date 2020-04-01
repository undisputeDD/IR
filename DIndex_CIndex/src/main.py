from DIndex_CIndex.src.search import di_search
from DIndex_CIndex.src.search import ci_search
from DIndex_CIndex.src.make_dict import making_d_index
from DIndex_CIndex.src.make_dict import making_c_index

'''This makes double-word index'''
#index, files = making_d_index()
'''This makes coord invert index'''
index, files = making_c_index()

f_writer = open('../result/output.txt', 'w')
f_writer.write(index.to_str())
f_writer.close()

'''This runs query searches for double-word index'''
#di_search(index, files)
'''This runs query searches for coord invert index'''
ci_search(index, files)
