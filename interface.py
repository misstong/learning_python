import inspect
from abc import ABCMeta, abstractmethod, abstractproperty

class IRectangle(metaclass=ABCMeta):
    @abstractproperty
    def width(self):
        return

    @abstractproperty
    def height(self):
        return

    @abstractmethod
    def area(self):
        """:return area"""

    @abstractmethod
    def perimeter(self):
        """return perimeter"""

    @classmethod
    def __subclasscheck__(cls, C):
        if cls is IRectangle:
            if all([
                any("area" in B.__dict__ for B in C.__mro__),
                any("perimeter" in B.__dict__ for B in C.__mro__),
                any("width" in B.__dict__ for B in C.__mro__),
                any("height" in B.__dict__ for B in C.__mro__),
            ]):
                return True
        return NotImplemented

def ensure_interface(function):
    signature = inspect.signature(function)
    parameters = signature.parameters

    def wrapped(*args,**kwargs):
        bound = signature.bind(*args, **kwargs)
        for name, value in bound.arguments.items():
            annotation = parameters[name].annotation

            if not isinstance(annotation, ABCMeta):
                continue

            if not isinstance(value, annotation):
                raise TypeError(
                    "{} does not implement {} interface"
                    "".format(value, annotation)
                )
        function(*args,**kwargs)
    return  wrapped

@ensure_interface
def draw_rectangle(rectangle: IRectangle):
    print(
        "{} x {} rectangle drawing".format(rectangle.width,rectangle.height)
    )


draw_rectangle('foo')