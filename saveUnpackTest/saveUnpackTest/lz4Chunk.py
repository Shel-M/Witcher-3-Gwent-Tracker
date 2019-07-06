import sys
from lz4 import block
from binaryReader import *

class lz4Chunk:
    compressedChunkSize = 0
    decompressedChunkSize = 0
    endOfChunkOffset = 0
    def __init__(self):
        return None

    def buildChunk(self, compressedSize, decompressedSize, endOffset):
        self.compressedChunkSize = compressedSize
        self.decompressedChunkSize = decompressedSize
        self.endOfChunkOffset = endOffset
        return self

    def read(self, input):
        inputData = bytes(self.compressedChunkSize)
        outputData = bytes(self.decompressedChunkSize)

        self.test(input, inputData)
        count = 0
        for eachByte in inputData:
            count += 1
        
        inputData = bytes(input.read(count))
        print(inputData)
        
        outputData = block.decompress(inputData)

        return outputData