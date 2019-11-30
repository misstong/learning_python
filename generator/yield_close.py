def foo():
	yield 'aaa'
	for i in range(2):
		yield i

def main():
	t = foo()
	print(t.__next__())
	print(t.__next__())
	print(t.__next__())
	print(t.__next__())
	t.close()
	# t.__next__()

main()