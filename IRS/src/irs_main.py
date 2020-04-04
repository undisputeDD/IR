from IRS.src.ReadEngine import ReadEngine
from IRS.src.SearchEngine import SearcEngine

read_engine = ReadEngine()
input_files, index = read_engine.read()
read_engine.write()
search_engine = SearcEngine()
search_engine.search(index, input_files)
