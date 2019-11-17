OPTIONS = {}

def register_option(name):
    return OPTIONS.setdefault(name, 1 << len(OPTIONS))

def has_option(options, name):
    return bool(options & name)

BLUE = register_option('BLUE')
RED = register_option('RED')
WHITE = register_option('WHITE')

