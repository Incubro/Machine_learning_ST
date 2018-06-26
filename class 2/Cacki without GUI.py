import tkinter as tk
def add(a,b):
	return a+b
def mult(a,b):
	return a*b
def sub(a,b):
	return a-b
def div(a,b):
	return a/b
def calc(arg):
	print('first number\n')
	a=input()
	print('first number')
	b=input()
	switch={
	1:add(a,b)
	2:mult(a,b)
	3:sub(a,b)
	4:div(a,b)
	}
	return switch.get(arg,"nothing")
print(calc(1))
#root=tk.Tk()
#root.geometry('400x400')
#root.title('Title of the box ')
#num1=tk.StringVar()
#entry = tk.Entry(root, textvariable=num1).grid(row=7,column=4)

#root.mainloop()
