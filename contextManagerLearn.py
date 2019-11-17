class ContextIllustration:
    def __enter__(self):
        print('entering context')

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('leaving context')
        if exc_type is None:
            print('with no error')
        else:
            print(f'with an error({exc_val})')

from contextlib import contextmanager

@contextmanager
def context_illustration():
    print('entering context')

    try:
        yield
    except Exception as e:
        print("leaving context")
        print(f'with an error ({e})')
        raise
    else:
        print('leaving context')
        print('with no error')

with ContextIllustration():
    print('aaa')