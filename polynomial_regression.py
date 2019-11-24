# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 19:34:15 2019

@author: Rohan
"""

''' Polynomial Regression '''

import numpy as np
import matplotlib.pyplot as plt
import sklearn
import pandas as pd

df = pd.read_csv('polynomial.csv')
plt.scatter(df.x, df.y)
x = df.iloc[:, 0:1].values
y = df.iloc[:, 1:2].values
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(x, y)

y_pred = model.predict(x)

plt.scatter(df.x, df.y)
plt.plot(x, y_pred, color='r')
print('Calculated R-Square for the training set: %0.2f' % model.score(x, y))

print(dir(sklearn.preprocessing))
from sklearn.preprocessing import PolynomialFeatures
polynomial_features = PolynomialFeatures(degree=2)
x_poly = polynomial_features.fit_transform(x)
model_2 = LinearRegression()
model_2.fit(x_poly, y)
y_pred_poly = model_2.predict(x_poly)
plt.plot(x, y_pred_poly, color='m')
print(model.coef_)
print(model.intercept_)
print('Calculated R-Square for the training set using polynomial regression: %0.2f' % model_2.score(x_poly, y))

polynomial_features = PolynomialFeatures(degree=3)
x_poly = polynomial_features.fit_transform(x)
model_3 = LinearRegression()
model_3.fit(x_poly, y)
y_pred_poly = model_3.predict(x_poly)
plt.plot(x, y_pred_poly, color='m')
print(model.coef_)
print(model.intercept_)
print('Calculated R-Square for the training set using polynomial regression: %0.2f' % model_3.score(x_poly, y))




