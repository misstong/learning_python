from pathlib import Path

lognames = Path('.').rglob("*.py")

def gen_open(path2):
	for path in path2:
		yield open(path,'rt')

def gen_cat(sources):
	print(type(sources))
	for src in sources:
		print("------src----",src)
		yield from src

logfiles = gen_open(lognames)
loglines = gen_cat(logfiles)

for i in loglines:
	print(i)
