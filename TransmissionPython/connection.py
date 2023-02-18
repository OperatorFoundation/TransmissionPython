class Connection:
    def read(self, size):
        pass

    def unsafeRead(self, size):
        pass

    def read(self, maxSize):
        pass

    def readWithLengthPrefix(self, prefixSizeInBits):
       pass

    # str or bytes are both acceptable
    def write(self, string):
        pass

    def writeWithLengthPrefix(self, data, prefixSizeInBits):
        pass

    def close(self):
        pass