class Files:
    def __init__(self):
        self.files = {}

    def add_file(self, fileID, file):
        self.files[fileID] = file

    def get_ids(self):
        return set(self.files.keys())


class File:
    def __init__(self, fileID):
        self.coord = []
        self.fileID = fileID

    def add_coord(self, coord):
        self.coord.append(coord)
