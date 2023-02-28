#
#  example.py
#
#
#  Created by Dr. Brandon Wiley on 2/19/23.
#

# We can import typing on desktop for IDE type-checking support, but it will fail when running on a microcontroller
try:
    from typing import *
except ImportError:
    pass  # ignore the error

from .pong import Pong

class Example:
    count: int

    def __init__(self):
        self.count = 0

    def increment(self):
        self.count = self.count + 1

    def arrayCheck(self, array: [str]) -> [str]:
        if self.count < 1:
            return []
        else:
            return array

    def add(self, addition: int):
        self.count = self.count + addition

    def ping(self) -> Pong:
        if self.count < 0:
            self.count = 0

        return Pong()

    def times(self, x: int) -> int:
        return self.count * x
