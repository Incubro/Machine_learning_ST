from random import randint
from sklearn import linear_model
from matplotlib import pyplot as plt
import numpy as np
from statistics import *
limit = 1000
count = 5
input_data = list()
output_data = list()
x1=list()
x2=list()
x3=list()
#Generating training set
for i in range(count):
	a=randint(0,limit)
	b=randint(0,limit)
	c=randint(0,limit)
	op=a+(2*b)+(3*c)
	x1.append(a);x2.append(b);x3.append(c)
	input_data.append([a,b,c])
	output_data.append(op)

plt.plot(x1,output_data,'-',marker='o',markersize='5',markerfacecolor='m')
plt.plot(x2,output_data,'-',marker='o',markersize='5',markerfacecolor='m')
plt.plot(x3,output_data,'-',marker='o',markersize='5',markerfacecolor='m')

#ML model - Linear Regression
model = linear_model.LinearRegression()
model.fit(input_data,output_data)
#model.fit(x1,output_data)

#Test New User Data
outcome = model.predict([[500,100,300]])
coeff = model.coef_
plt.plot(outcome,'rs')

print('Outcome : {}\nCoefficients : {}'.format(outcome,coeff))

x=[1,2,3,4,5,6,7]
y=[7,6,5,4,3,2,1]

xs=np.array(input_data, dtype=np.float64)
ys=np.array(output_data, dtype=np.float64)

def slope_intercept(xs,ys):
	#m=(((mean(xs)*mean(ys)) - mean(xs*ys)) /(mean(xs)**2 - mean(xs*xs)))
	m=2;b=3
	#b=mean(ys) - m*mean(xs)

	return m,b


m,c=slope_intercept(xs,ys)

reg_line=list()

for x in xs:
	reg_line.append((m*x)+c)

#plt.scatter(xs,ys,color='#000000')
plt.plot(xs,reg_line,'g')
plt.show()