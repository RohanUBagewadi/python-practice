# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 16:31:25 2019

@author: Rohan
"""

''' Multiple Linear regression '''
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import sklearn

from sklearn.datasets import load_boston
Boston_data = load_boston()
print(Boston_data.DESCR)
print(Boston_data.feature_names)
print(Boston_data.data)
dataset = pd.DataFrame(Boston_data.data, columns=Boston_data.feature_names)
dataset['MEDV'] = Boston_data.target

dataset.info() # To check data type of each field
print(dataset.isnull().sum()) # To see if there are any missing values in the dataset

corr = dataset.corr() # Computes the pairwise correlation of columns
print(corr.iloc[-1, :]) # Taking only the lasr row to find the dependicies

print(dataset.corr().abs().nlargest(3, 'MEDV').index) # prints the top 3 features that has the highest correlation

plt.scatter(dataset['LSTAT'], dataset['MEDV'], marker='o')
plt.xlabel('LSTAT')
plt.xlabel('MEDV')

plt.scatter(dataset['RM'], dataset['MEDV'], marker='+')
plt.xlabel('RM')
plt.xlabel('MEDV')

from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure(figsize=(18,15))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(dataset['LSTAT'], dataset['RM'],dataset['MEDV'])
ax.set_xlabel('LSTAT')
ax.set_ylabel('RM')
ax.set_zlabel('MEDV')
plt.show()
X = dataset[['LSTAT', 'RM']]
y = dataset[['MEDV']]

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder_X = LabelEncoder()
X_train[:, 3] = labelencoder_X.fit_transform(X_train[:, 3])
onehotencoder = OneHotEncoder(categorical_features = [0])
X_train[:, 3] = onehotencoder.fit_transform(X_train[:, 3]).toarray()

from sklearn.preprocessing import StandardScaler
#print(dir(sklearn.preprocessing))
standard_scaler = StandardScaler()
X_train = standard_scaler.fit_transform(X_train)

from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(X_train, y_train)

y_predict = model.predict(X_test)

print('R-Square: %.4f' % model.score(X_test, y_test))
from sklearn.metrics import mean_squared_error
mse = mean_squared_error(y_test, y_predict)
print(mse)


from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder_X = LabelEncoder()
X[:, 0] = labelencoder_X.fit_transform(X[:, 0])
onehotencoder = OneHotEncoder(categorical_features = [0])
X = onehotencoder.fit_transform(X).toarray()