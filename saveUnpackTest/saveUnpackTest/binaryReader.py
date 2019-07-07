from struct import *

class binaryReader:
    def __init__(self, input):
        self.stream = input

    def readBytes(self, length):
        return self.stream.read(length)
    #--
    def readInt16(self):
        return self.unpack('h', 2)
    def readInt32(self):
        return self.unpack('i', 4)

    def readString(self, length):
        return self.unpack(str(length) + 's', length)

    def unpack(self, format, length = 1):
        return unpack(format, self.readBytes(length))[0]

    def baseStream(self):
        return self.stream

class BinaryStream:
    def readByte(self):
        return self.base_stream.read(1)

    def readBytes(self, length):
        return self.base_stream.read(length)

    def readChar(self):
        return self.unpack('b')

    def readUChar(self):
        return self.unpack('B')

    def readBool(self):
        return self.unpack('?')

    def readInt16(self):
        return self.unpack('h', 2)

    def readUInt16(self):
        return self.unpack('H', 2)

    def readInt32(self):
        return self.unpack('i', 4)

    def readUInt32(self):
        return self.unpack('I', 4)

    def readInt64(self):
        return self.unpack('q', 8)

    def readUInt64(self):
        return self.unpack('Q', 8)

    def readFloat(self):
        return self.unpack('f', 4)

    def readDouble(self):
        return self.unpack('d', 8)

    def readString(self):
        length = self.readUInt16()
        return self.unpack(str(length) + 's', length)

    def unpack(self, fmt, length = 1):
        return unpack(fmt, self.readBytes(length))[0]
