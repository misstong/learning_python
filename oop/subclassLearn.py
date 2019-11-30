"""
make a duck-typed class look like a subclass
issubclass(B,A) == > True
"""

import abc
class A(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def play(self):
        pass

    @classmethod
    def __subclasshook__(cls,C):
        if cls is A:
            attrs = set(dir(C))
            if set(cls.__abstractmethods__) <= attrs:
                return True
        return NotImplemented


class B:
    def play(self):
        pass

