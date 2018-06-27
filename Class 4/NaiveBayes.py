from sklearn import naive_bayes 
import numpy as np
import csv
import pandas as pd

#assigning predictor and target variables
field=['X1','X2']
Y = np.array([1,4,3,4,3,4,3,4,3,3,4,3,3])
#Y = np.array([[3],[4],[3],[4],[3],[4],[3],[4],[3],[3],[4],[3]])
X= np.array([[-3,7],[1,5], [1,2], [-2,0], [2,3], [-4,0], 
	[-1,1], [1,1], [-2,2], [2,7], [-4,1], [-2,7],[2,3]])
with open ('filename.csv','w') as cs:
	csfile=csv.writer(cs)
	csfile.writerow(field)
	csfile.writerows(X)





df=pd.read_csv('filename.csv')
df.insert(2,'Y','')
#print(len(Y))
for i in range(len(Y)):
	#[row,column]
	df.iloc[i,2]=Y[i]
print(df)
df.to_csv('filename.csv')





#Create a Gaussian Classifier
model = naive_bayes.GaussianNB()

# Train the model using the training sets 
model.fit(X, Y)
x1=input('enter your num \n')
x2=input('enter your num\n')
x1=int(x1)
x2=int(x2)

#Predict Output 
predicted= model.predict([[x1,x2]])
print (predicted)