def add(a,b):
	return a+b
def mul(a,b):
	return a*b
def sub(a,b):
	return a-b
def div(a,b):
	return a/b
def calc(arg):
	a=4
	b=3
	switcher = {
	0:add(a,b),
	1:mul(a,b),
	2:sub(a,b),
	3:div(a,b),
	}
	return switcher.get(arg,"nothing")
print(calc(1))