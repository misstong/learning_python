import logging

logging.basicConfig()
class RevealingMeta(type):
    def __new__(mcs,name,bases,namespace, **kwargs):
        logging.warning(f'{mcs} __new__ called')
        return super().__new__(mcs,name,bases,namespace)

    @classmethod
    def __prepare__(mcs, name, bases,**kwargs):
        logging.warning(f'{mcs} __prepared__ called')
        return super().__prepare__(name,bases,**kwargs)

    def __init__(cls,name,bases,namespace,**kwargs):
        logging.warning(f'{cls} __init__ called')
        super().__init__(name,bases,namespace)

    def __call__(cls, *args, **kwargs):
        logging.warning(f'{cls} __call__ called')
        return super().__call__(*args,**kwargs)



class RevealingClass(metaclass=RevealingMeta):
    def __new__(cls, *args, **kwargs):
        logging.warning(f'{cls} __new__ called')
        return super().__new__(cls)

    def __init__(self):
        logging.warning(f'{self} __init__ called')
        super().__init__()

"""
subclass also invoke metaclass
"""
class RevealingSubclass(RevealingClass):
    pass
instance = RevealingClass()