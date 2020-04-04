from IRS.src.File import File

class PostList:

    def __init__(self):
        self.post_list = {}

    def add_file_coord(self, fileID, coord):
        if fileID not in self.post_list.keys():
            current_file = File(fileID)
            current_file.add_coord(coord)
            self.post_list[fileID] = current_file
        else:
            self.post_list[fileID].add_coord(coord)
