def main():
	r = (yield)
	print(r)

c = main()
c.send(None)
c.send('1')
