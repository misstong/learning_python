
"""only apply for hashable"""
def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
        seen.add(item)

"""modified version"""
def dedupe2(items,key=None):
    seen = set()
    for item in items:
        val = item if key == None else key(item)
        if val not in seen:
            yield item
        seen.add(val)

a = [{'x':1,'y':2},{'x':1,'y':3},{'x':1,'y':2},{'x':2,'y':4}]
print(list(dedupe2(a,key = lambda d:(d['x'],d['y']))))
