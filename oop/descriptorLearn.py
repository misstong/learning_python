"""
data descriptor:very hard to understand
"""


import logging
#using logging for practice
logger = logging.getLogger(__name__)
handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s-%(levelname)s-%(message)s')
handler.setFormatter(formatter)
handler.setLevel(logging.DEBUG)
logger.setLevel(logging.DEBUG)
logger.addHandler(handler)

class RevealAccess(object):
    """A data descriptor that sets and returns values
        normally and prints a message logging their access.
    """
    def __init__(self,initval=None,name='var'):
        self.val = initval
        self.name = name

    def __get__(self, obj, objtype):
        logger.debug(f'Retrieving {self.name}')
        return self.val

    def __set__(self,obj,val):
        logger.debug(f'Updating {self.name}')
        self.val = val

class MyClass(object):
    x = RevealAccess(10,'var "x"')
    y = 5

m = MyClass()
m.x
m.x = 20
m.x
m.y