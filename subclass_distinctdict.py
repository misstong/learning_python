from collections import UserDict

class DistinctError(ValueError):
    """Raised when duplicate value is added to a distinctdict"""


class distinctDict(UserDict):
    """Dictionary that does not accept duplicate values"""
    def __setitem__(self, key, value):
        if value in self.values():
            if (key not in self or (key in self and self[key] != value)):
                raise DistinctError("This value already exists for different key")
        super().__setitem__(key,value)

from collections import UserList

class Folder(UserList):
    def __init__(self,name):
        self.name = name

    def dir(self,nesting=0):
        offset = " " * nesting
        print('%s%s/' % (offset, self.name))

        for element in self:
            if hasattr(element, 'dir'):
                element.dir(nesting + 1)
            else:
                print('%s %s'% (offset, element))


"""
__setitem__: implement this to allow [] operator
"""

class classCanSetItem:
    def __init__(self):
        self.map = {}

    def __setitem__(self, key, value):
        self.map[key] = value

    def __repr__(self):
        return  self.map.__repr__()

