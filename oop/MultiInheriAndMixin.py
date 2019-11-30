class Animal:
    def eat(self):
        print('Animal can eat')

class Bird(Animal):
    def eat(self):
        # super().eat()
        print('Bird can eat')
        super().eat()

class Flyable(Animal):
    def eat(self):
        # super().eat()
        print('Flyable eat')
        super().eat()

class FlyingBird(Flyable,Bird):
    pass

# FlyingBird().eat()


class BaseClass:
    def call_me(self):
        print('call base')

class LeftSubclass(BaseClass):
    def call_me(self):
        BaseClass().call_me()
        print('call left')

class RightSubclass(BaseClass):
    def call_me(self):
        BaseClass().call_me()
        print('call right')

class Subclass(RightSubclass,LeftSubclass):
    def call_me(self):
        LeftSubclass().call_me()
        RightSubclass().call_me()
        print('subclass')

# Subclass().call_me()
from collections import Container
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

    def __contains__(self,x):
        return True

    

print(issubclass(B,A))
print(issubclass(B,Container))
