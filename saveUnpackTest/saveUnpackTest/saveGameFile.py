from lz4File import lz4File
from binaryReader import *


class saveGameFile:
    class rbEntry(object):
        size = int()
        offset = int()
        def __init__(self, size, offset):
            self.size = size
            self.offset = offset
            return None

    typeCode1 = int()
    typeCode2 = int()
    typeCode3 = int()

    headerStartOffset = int()
    variableTableOffset = int()
    stringTableFooterOffset = int()
    stringTableOffset = int()
    rbSectionOffset = int()
    nmSectionOffset = int()

    def __init__(self):
        return None

    def read(self, path):
        compressedInput = open(path, mode = 'rb')
        decompressedInput = lz4File().decompress(compressedInput)
        reader = binaryReader(decompressedInput)

        self.readHeader(reader)
        self.readFooter(reader)
        self.readStringTable(reader)

        return self

    def readHeader(self, reader):
        self.headerStartOffset = reader.baseStream().tell()

        fileCheck = reader.readString(4)
        if fileCheck != b'SAV3':
            raise Exception("Malformed .sav file!")

        self.typeCode1 = reader.readInt32()
        self.typeCode2 = reader.readInt32()
        self.typeCode3 = reader.readInt32()

    def readFooter(self, reader):
        reader.baseStream().seek(-6,2)
        self.variableTableOffset = reader.readInt32()
        self.stringTableFooterOffset = self.variableTableOffset - 10
        fileCheck = reader.readString(2)
        if fileCheck != b'SE':
            raise Exception("Malformed .sav file!")
        
    def readStringTable(self, reader):
        reader.baseStream().seek(self.stringTableFooterOffset)
        self.nmSectionOffset = reader.readInt32()
        self.rbSectionOffset = reader.readInt32()
        self.readNmSection(reader)
        self.readRbSection(reader)
        self.readVariableNameSection(reader)

    def readNmSection(self, reader):
        reader.baseStream().seek(self.nmSectionOffset)
        fileCheck = reader.readString(2)
        if fileCheck != b'NM':
            raise Exception("Malformed .sav file!")

        self.stringTableOffset = reader.baseStream().tell()

    def readRbSection(self, reader):
        reader.baseStream().seek(self.rbSectionOffset)
        fileCheck = reader.readString(2)
        if fileCheck != b'RB':
            raise Exception("Malformed .sav file!")
        count = reader.readInt32()
        rbEntries = array(rbEntry)
        for i in range(count):
            rbEntries.append(rbEntry(reader.readInt16(), reader.readInt32()))

    def readVariableNameSection(self, reader):
        reader.baseStream().seek(self.stringTableOffset)