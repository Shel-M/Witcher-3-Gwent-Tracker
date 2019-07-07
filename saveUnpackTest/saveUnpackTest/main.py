from lz4File import lz4File
from binaryReader import *
from saveGameFile import *

path = '.\\bin\\big.sav'

saveGame = saveGameFile().read(path)



'''
compressedInput = open(path, mode = 'rb')
decompressedInput = lz4File().decompress(compressedInput)
reader = binaryReader(decompressedInput)

with open(".\\bin\\outfile.txt", 'wb+') as outfile:
    outfile.write(decompressedInput.read(-1))

'''