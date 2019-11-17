"""
reference link:https://realpython.com/primer-on-python-decorators/#fancy-decorators
"""

"""
No param-decorator
"""

def non_param_decorator(func):
    def wrapper(*args,**kwargs):
        rst = func(*args,**kwargs)
        return  rst
    return  wrapper

"""
Param-decorator
"""
def param_decorator(param):
    def _wrapper(func):
        def _wrapper(*args, **kwargs):
            """some where uses param"""
            rst = func(*args, **kwargs)
            return  rst
        return _wrapper
    return _wrapper


"""
decorator which can have or not have params
"""
def flexible_decorator(_func=None,*,arg1=None):
    def _wrapper(func):
        def _wrapper(*args, **kwargs):
            """some where uses param"""
            rst = func(*args, **kwargs)
            return  rst
        return _wrapper
    if _func == None:
        return  _wrapper
    else:
        return  _wrapper(_func)

"""
1. decorate function,method,class almost the same
2. decorator can also implemented as a class instead of a function
3. use cases for decorator:
    singleton---decorate a class,just a stateful decorator
    count function calls---almost same as singleton, a stateful decorator
    cache---stateful decorator
"""