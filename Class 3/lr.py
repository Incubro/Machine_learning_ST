from sklearn import linear_model as lm
import random
from matplotlib import pyplot as plt
count =100
limit =1000

input_data=list()
output_data=list()

for i in range(0,count):
	x1=random.randint(0,limit)
	x2=random.randint(0,limit)
	x3=random.randint(0,limit)
	y=x1+3*x2+4*x3
	input_data.append([x1,x2,x3])
	output_data.append([y])

plt.plot(input_data,output_data,'o')

obj=lm.LinearRegression()
obj.fit(input_data,output_data)
input1=int(input());input2=int(input());input3=int(input())

outcome=obj.predict([[input1,input2,input3]])
plt.plot(outcome,'ys')
plt.show()
print(outcome)

#x1+3(x2)+4(x3)=y

