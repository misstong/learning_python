
def foo():
	for i in [1,2,3]:
		yield i

def foo2():
	yield from [1,2,3]


for i in foo():
	print(i)

for i in foo2():
	print(i)