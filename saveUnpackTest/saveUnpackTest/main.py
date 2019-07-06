from Lz4File import lz4File

path = '.\\bin\\latest.sav'

compressedInput = open(path, mode = 'rb')
decompressedInput = lz4File().decompress(compressedInput)
