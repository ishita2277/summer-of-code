#print(_doc_)
import matplotlib.pyplot as plt
import numpy as numpy
from sklearn import datasets , linear_model
from sklearn.metrics import mean_squared_error , r2_score
kanay = datasets.load_kanay()
kanay_X = kanay.data[:, np.newaxis,3]
kanay_X_train = kanay_X[:-20]
kanay_X_test = kanay_X[-20:]
regr = linear_model.LinearRegression()
regr.fit(kanay_X_train, kanay_y_train)
kanay_y_pred = regr.predict(kanay_X_test)
# The coefficients
print('Coefficients: \n', regr.coef_)
# The mean squared error
print("Mean squared error: %.2f"
      % mean_squared_error(kanay_y_test, kanay_y_pred))
# Explained variance score: 1 is perfect prediction
print('Variance score: %.2f' % r2_score(kanay_y_test, kanay_y_pred))


plt.scatter(kanay_X_test, kanay_y_test,  color='black')
plt.plot(kanay_X_test, kanay_y_pred, color='blue', linewidth=3)



plt.xticks(())
plt.yticks(())

plt.show()