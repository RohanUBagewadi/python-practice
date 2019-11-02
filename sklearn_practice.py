# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 12:46:40 2019

@author: Rohan
"""
''' Sklearn library practice '''

import numpy as np
import sklearn
import pandas as pd
import matplotlib.pyplot as plt

'''' 1)
        Using Scikit learn datasets '''
        
from sklearn import datasets
iris = datasets.load_iris() # Loads the datasets
print(iris.DESCR) # Prints the discription of the dataset
print(iris.data) # Prints the entire dataset
print(iris.feature_names) # Prints the feature name
print(iris.target_names) # Prints the label names
print(iris.target) # Prints the output labels

# It's always usefull to convert the data to a Pandas dataframe
df = pd.DataFrame(iris.data)
print(df.head())

''' 2)
        Generating own datasets'''

'''' 2.a)
        Generating Linearly Distributed Datasets'''
        
from sklearn.datasets.samples_generator import make_regression
X, y = make_regression(n_samples=100, n_features=1, n_targets=1, noise=5.4)
plt.scatter(X, y, color='m', marker='s')
plt.grid(True)

'''' 2.b)
        Clusterred Datasets'''
        
from sklearn.datasets import make_blobs
X, y = make_blobs(500, centers=4)
rgbm = np.array(['r', 'g', 'y', 'm'])
# Plot the blobs using a scatter plot and useing colour coding
plt.scatter(X[:,0], X[:, 1], color=rgbm[y])

'''' 2.b)
        Clusterred Datasets in Circular form'''

from sklearn.datasets import make_circles
X, y = make_circles(n_samples=150, noise=0.1)
plt.scatter(X[:, 0], X[:, 1], marker='+')

''' 3)
        Using Linear Regression'''

#---------------Dataset---------------      
heights = [[1.6], [1.65], [1.7], [1.73], [1.8]]
weights = [[60], [65], [72.3], [75], [80]]


#---------------Defining the model--------
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(X=heights, y=weights) # Creates a linear regression model between X and y
y_predict = model.predict([[1.75]])


#---------------Plotting the model---------

plt.plot(heights, weights, 'k.')
plt.axis([1.5, 1.85, 50, 90])
plt.title('Weigths plotted against Heights')
plt.xlabel('Heights in meters')
plt.ylabel('Weights in Kg')
plt.plot(model.predict(heights))
plt.grid(True)

#-------Getting the gradient and intersept of the Linear Regression Line--------

plt.axis([0, 1.85, -90, 90])
plt.plot(model.predict([[0], [1.8]]))
print(round(model.intercept_[0],2)) # prints x-intersept
print(round(model.coef_[0][0],2)) # Prints the gradient of the linear regression

#-----------Examining the performance of the model by calculating the residual sum of squares
print('Residual sum of squares: %.2f' % np.sum(weights-model.predict(heights)**2))

#-----------Evaluating the model using a Test Dataset------------
#-----------Data Pre-Processing-------

from sklearn.datasets import load_iris
data = load_iris()
data_set = pd.DataFrame(data.data, columns=data.feature_names)

# Checking for Nullvalues in the dataset
data_set = pd.read_csv('name.csv')
data_set.isnull().sum() # Return number of NaN values column wise

# Replacing the NaN values with the mean of the column
data_set.iloc[:, 1] = data_set.iloc[:, 1].fillna(data_set.iloc[:, 1].mean())
print(data_set)

data_set = data_set.dropna() # Drops all the rows with NaN
data_set = data_set.reset_index(drop=True) # To reset index after droping

print(data_set.duplicated(keep=False)) # To find the duplicate rowwise
print(data_set[data_set.duplicated(keep=False)])
data_set.drop_duplicates(keep='First', inplace=True)# To remove dublicates and keep the first

data_set = data_set.values.astype(float) # Converting the dataframe into values
from sklearn.preprocessing import MinMaxScaler
min_max_scalar = MinMaxScaler()
data_set_scaled = min_max_scalar.fit_transform(data_set)

# Normalizing the columns






