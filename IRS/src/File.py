class File:

    def __init__(self, fileID):
        self.fileID = fileID
        self.coord_list = []

    def add_coord(self, coord):
        self.coord_list.append(coord)
