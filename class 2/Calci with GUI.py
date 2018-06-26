from tkinter import *
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
root=Tk()
root.geometry('500x500')
root.title("Calculator")
#main logic function
def call_result(labelResult,n1,n2,n3):
	num1=n1.get()
	num2=n2.get()
	option=n3.get()
	result = calc(int(option),int(num1),int(num2))
	labelResult.config(text='Result %f'%result)
	return

#creates stringvariables which stores the 
num1=StringVar()
num2=StringVar()
num3=StringVar()
option=IntVar()

#creates Entry point for 3 inputs
entry1=Entry(root,textvariable=num1).grid(row=0,column=1)
entry2=Entry(root,textvariable=num2).grid(row=1,column=1)
entry3=Entry(root,textvariable=num3).grid(row=2,column=1)

# creates the label point for result
labelResult = Label(root)
labelResult.grid(row=8, column=2)

#Radio buttons
R1=Radiobutton(root,text="ADDITION",variable=option,value=0).grid(row=3,column=1)
R2=Radiobutton(root,text="MULTIPLICATION",variable=option,value=1).grid(row=4,column=1)
R3=Radiobutton(root,text="SURTACTION",variable=option,value=2).grid(row=5,column=1)
R4=Radiobutton(root,text="DIVISION",variable=option,value=3).grid(row=6,column=1)

#creates the labels of the text written for the GUI
label1=Label(root,text="Enter First num").grid(row=0,column=0)
label2=Label(root,text="Enter Second num").grid(row=1,column=0)
label3=Label(root,text="Choice: 0-add,1-mult,3=sub,4=div").grid(row=2,column=0)
call_result = partial(call_result, labelResult, num1, num2, option)
buttonCal = Button(root, text="Calculate", command=call_result).grid(row=4, column=0)

root.mainloop()