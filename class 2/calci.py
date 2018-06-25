import tkinter as tk
from functools import partial
def add(a,b):
	return a+b
def mul(a,b):
	return a*b
def sub(a,b):
	return a-b
def div(a,b):
	return a/b
def calc(arg,a,b):
	switcher = {
	0:add(a,b),
	1:mul(a,b),
	2:sub(a,b),
	3:div(a,b),
	}
	return switcher.get(arg,"nothing")
#tkinter initialization
root=tk.Tk()
root.geometry('400x400')
root.title("Calculator")
#main logic function
def call_result(labelResult,n1,n2,n3):
	num1=n1.get()
	num2=n2.get()
	num3=n3.get()
	result = calc(int(num3),int(num1),int(num2))
	labelResult.config(text='Result %d'%result)
	return

#creates stringvariables which stores the 
num1=tk.StringVar()
num2=tk.StringVar()
num3=tk.StringVar()

#creates Entry point for 3 inputs
entry1=tk.Entry(root,textvariable=num1).grid(row=0,column=1)
entry2=tk.Entry(root,textvariable=num2).grid(row=1,column=1)
entry3=tk.Entry(root,textvariable=num3).grid(row=2,column=1)

# creates the label point for result
labelResult = tk.Label(root).grid(row=8, column=2)

#creates the labels of the text written for the GUI
label1=tk.Label(root,text="Enter First num").grid(row=0,column=0)
label2=tk.Label(root,text="Enter Second num").grid(row=1,column=0)
label3=tk.Label(root,text="Choice: 0-add,1-mult,3=sub,4=div").grid(row=2,column=0)
call_result = partial(call_result, labelResult, num1, num2, num3)
buttonCal = tk.Button(root, text="Calculate", command=call_result).grid(row=4, column=0)

root.mainloop()