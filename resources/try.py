import tkinter as tk
from functools import partial
from sklearn import neighbors
X = [[181, 80, 44], [177, 70, 43], [160, 60, 38], [154, 54, 37], [166, 65, 40],
     [190, 90, 47], [175, 64, 39],
     [177, 70, 40], [159, 55, 37], [171, 75, 42], [181, 85, 43]]

Y = ['male', 'male', 'female', 'female', 'male', 'male', 'female', 'female',
     'female', 'male', 'male']
clf = neighbors.KNeighborsClassifier()
clf = clf.fit(X, Y)
prediction = clf.predict([[170, 60, 33]])
def call_result(label_result, n1, n2, n3):
    num1 = (n1.get())
    num2 = (n2.get())
    num3 = (n3.get())
    result = clf.predict([[int(num1),int(num2),int(num3)]])
    label_result.config(text="Result is %s" %result)
    return
 
root = tk.Tk()
root.geometry('400x200+100+200')
root.title('tkinter example')
 
number1 = tk.StringVar()
number2 = tk.StringVar()
number3 = tk.StringVar()
 
labelTitle = tk.Label(root, text="tkinter example").grid(row=0, column=2)
labelNum1 = tk.Label(root, text="Enter a number").grid(row=1, column=0)
labelNum2 = tk.Label(root, text="Enter another number").grid(row=2, column=0)
labelNum3 = tk.Label(root, text="Enter third number").grid(row=3, column=0)

labelResult = tk.Label(root)
labelResult.grid(row=8, column=2)
 
entryNum1 = tk.Entry(root, textvariable=number1).grid(row=1, column=2)
entryNum2 = tk.Entry(root, textvariable=number2).grid(row=2, column=2)
entryNum3 = tk.Entry(root, textvariable=number3).grid(row=3, column=2)
call_result = partial(call_result, labelResult, number1, number2, number3)
buttonCal = tk.Button(root, text="Calculate", command=call_result).grid(row=4, column=0)
root.mainloop()