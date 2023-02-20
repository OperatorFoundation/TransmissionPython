import busio
import json
import time

from .connection import Connection
from .length_prefix_helper import readWithLengthPrefixHelper, writeWithLengthPrefixHelper

class SerialConnection(Connection):
    maxRetries = 10

    def __init__(self, tx, rx, baudrate=None):
        if baudrate:
            self.serial = busio.UART(tx, rx, baudrate=baudrate)
        else:
            self.serial = busio.UART(tx, rx)

    def readSize(self, size):
        result = self.unsafeRead(size)

        if not result:
            raise Exception("read was empty")

        if len(result) != size:
            raise Exception("read was short")

        return result

    def unsafeRead(self, size):
        result = self.serial.read(size)

        retries = 0
        while (not result) and retries < self.maxRetries:
            time.sleep(1)
            result = self.serial.read(size)

        return result

    def readMaxSize(self, maxSize):
        result = self.serial.read(maxSize)
        if not result:
            return b''
        else:
            return result

    def readWithLengthPrefix(self, prefixSizeInBits):
       return readWithLengthPrefixHelper(self, prefixSizeInBits)

    def read(self, readType):
        if readType == bytes:
            return self.readWithLengthPrefix(64)
        elif readType == str:
            result = self.readWithLengthPrefix(64)
            return str(result)
        else:
            result = self.readWithLengthPrefix(64)
            obj = json.loads(str(result))
            if isinstance(obj, readType):
                return obj
            else:
                raise Exception("Wrong type")

    def write(self, obj):
        if type(obj) == str:
            self.serial.write(bytes(obj))
            return True
        elif type(obj) == bytes:
            self.serial.write(obj)
            return True
        else:
            return self.writeWithLengthPrefix(bytes(json.dumps(obj)), 64)

    def writeWithLengthPrefix(self, data, prefixSizeInBits):
        return writeWithLengthPrefixHelper(self, data, prefixSizeInBits)

    def close(self):
        pass