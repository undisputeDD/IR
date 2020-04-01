class Files:
    def __init__(self):
        self.files = {}

    def add_file(self, fileID, file):
        self.files[fileID] = file

    def get_ids(self):
        return set(self.files.keys())
