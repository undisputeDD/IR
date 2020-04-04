import glob
import re
from IRS.src.PostList import PostList
from IRS.src.File import File
from IRS.src.Index import Index
import time


class ReadEngine:

    def __init__(self):
        self.word_file = Index()

    def read(self):
        start_time = time.time()

        pattern = re.compile("(?<=[> \n\t])*([a-z0-9][a-z0-9']*-?[a-z0-9']*)(?=[< \n\t])*")
        input_files = glob.glob('/Users/apple/PycharmProjects/IR/IRS/resources/*')
        fileID = 1
        all_terms = 0
        for data_file in input_files:
            print(data_file)
            file = open(data_file)
            data = file.read().lower()
            data = re.findall(pattern, data)
            all_terms += len(data)
            coord = 1
            for term in data:
                if term not in self.word_file.index.keys():
                    '''If there is no term in index(and Posting List consequently), we are creating a new one'''
                    post_list = PostList()
                    post_list.add_file_coord(fileID, coord)

                    self.word_file.index[term] = post_list
                else:
                    '''When we have term in index, we check if there was current fileID in Posting List of a term
                       If not, we add it with current coord. If yes, we just add coord.(It`s made in PostList)'''
                    self.word_file.index[term].add_file_coord(fileID, coord)
                coord += 1
            file.close()
            fileID += 1

        unique_terms = len(self.word_file.index.keys())
        time_spent = time.time() - start_time

        print('All terms:', all_terms)
        print('Unique terms:', unique_terms)
        print('Time spent for reading:', time_spent)

        return input_files, self.word_file

    def write(self):
        start_time = time.time()
        if len(self.word_file.index.keys()) == 0:
            return False
        with open('result/output.txt', 'wt') as f_writer:
            f_writer.write(self.word_file.to_str())
        print('Time spent for writing:', time.time() - start_time)
