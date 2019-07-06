from lz4Header import *
from lz4Table import *
from lz4Chunk import *
from _io import BytesIO

class lz4File:
    def decompress(self, input):
        header = lz4Header().read(input) 
        table = lz4Table().read(input, header.chunkCount)
        input.seek(header.headerSize, 0)

        data = bytes(header.headerSize + sum(chunk.decompressedChunkSize for chunk in table))
        memoryStream = BytesIO(data)
        memoryStream.seek(header.headerSize, 0)

        for chunk in table:
            chunk.read(input)
