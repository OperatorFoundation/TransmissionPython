from .listener import Listener
from .serial_connection import SerialConnection

class SerialListener(Listener):
    def __init__(self, tx, rx, baudrate=None):
        self.tx = tx
        self.rx = rx
        self.baudrate = baudrate

    def accept(self):
        return SerialConnection(self.tx, self.rx, self.baudrate)

    def close(self):
        pass