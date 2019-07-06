from binaryReader import *

class lz4Header:
    chunkCount = 0
    headerSize = 0

    def __init__(self):
        return None

    def read(self, input):
        reader = binaryReader(input)

        header = reader.readString(4)

        Lz4FileHeader = reader.readString(4)

        self.chunkCount = reader.readInt32()
        self.headerSize = reader.readInt32()

        return self