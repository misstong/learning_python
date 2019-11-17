
d = {}
d.setdefault('a',[]).append(1)

from collections import defaultdict
d = defaultdict(list)
d['a'].append(1)