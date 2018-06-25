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
#prediction = clf.predict([[170, 60, 33]])

def call_result(label_result,n1,n2,n3):
	num1=(n1.get())
	num2=(n2.get())
	num3=(n3.get())
	result=clf.predict([[int(num1),int(num2),int(num3)]])
	label_result.config(text='Result is %s'%result)
	return

root =tk.Tk()