import struct

def readWithLengthPrefixHelper(connection, prefixSizeInBits):
    prefixSizeInBytes = prefixSizeInBits / 8
    lengthBytes = connection.readSize(prefixSizeInBytes)
    if not lengthBytes or (len(lengthBytes) != prefixSizeInBytes):
        raise Exception("prefix read failed")

    if prefixSizeInBits == 8:
        length = struct.unpack("B", lengthBytes)
    elif prefixSizeInBits == 16:
        length = struct.unpack("!H", lengthBytes)
    elif prefixSizeInBits == 32:
        length = struct.unpack("!L", lengthBytes)
    elif prefixSizeInBits == 64:
        length = struct.unpack("!Q", lengthBytes)
    else:
        raise Exception("bad prefix size")

    return connection.readSize(length)

def writeWithLengthPrefixHelper(connection, prefixSizeInBits, data):
    length = len(data)

    if prefixSizeInBits == 8:
        lengthBytes = struct.pack("B", length)
    elif prefixSizeInBits == 16:
        lengthBytes = struct.pack("!H", length)
    elif prefixSizeInBits == 32:
        lengthBytes = struct.pack("!L", length)
    elif prefixSizeInBits == 64:
        lengthBytes = struct.pack("!Q", length)
    else:
        raise Exception("bad prefix size")

    writeData = lengthBytes + data
    connection.write(writeData)