from sklearn import datasets, linear_model
from matplotlib import pyplot as plt
import numpy as np
from sklearn.metrics import mean_squared_error, r2_score

datasets = datasets.load_diabetes()

X = datasets.data[:, np.newaxis,2]

X_train = X[:-20]
X_test = X[-20:]

y_train = datasets.target[:-20]
y_test = datasets.target[-20:]

regr = linear_model.LinearRegression()
regr.fit(X_train,y_train)
y_pred = regr.predict(X_test)

print('Coefficients: \n', regr.coef_)

print("Mean squared error: %.2f"% mean_squared_error(y_test, y_pred))
print('Variance score: %.2f' % r2_score(y_test, y_pred))

plt.scatter(X_test, y_test,  color='black')
plt.plot(X_test, y_pred, color='blue', linewidth=3)
plt.show()


