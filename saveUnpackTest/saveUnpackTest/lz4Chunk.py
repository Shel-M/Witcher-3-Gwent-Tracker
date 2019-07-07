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

        count = 0
        uncompressedSize = 0
        for eachByte in inputData:
            count += 1
        for eachByte in outputData:
            uncompressedSize += 1
        
        inputData = bytes(input.read(count))
        
        outputData = block.decompress(inputData,uncompressedSize,return_bytearray = True)
        
        return outputData