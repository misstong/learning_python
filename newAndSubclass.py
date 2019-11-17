class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        print(cls)
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance


class SingleSubclass(Singleton):
    pass
c = SingleSubclass()
print(c)
a = Singleton()
b = Singleton()
print(a == b)
print(a)
print(b)


