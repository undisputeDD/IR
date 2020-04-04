from IRS.src.ReadEngine import ReadEngine

read_engine = ReadEngine()
input_files, index = read_engine.read()
read_engine.write()
