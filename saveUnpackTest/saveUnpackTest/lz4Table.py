from binaryReader import *
from lz4Chunk import *

class lz4Table:
    chunks = []
    def __init__(self):
        return None

    def read(self, input, chunkCount):
        reader = binaryReader(input)

        for i in range(chunkCount):
            self.chunks.append(lz4Chunk().buildChunk(reader.readInt32(), reader.readInt32(), reader.readInt32()))

        return self.chunks
