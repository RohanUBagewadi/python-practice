# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 20:12:15 2019

@author: rubag
"""

''' Numpy library practice'''

import numpy as np
a = np.array([1, 2, 3]) # Creates a rank 1 array
print(type(a))
print(a.shape) # Prints the shape of the array
print(a[0], a[2]) # Prints the array 0th and 3rd elements
a[0] = 5 # The elements of the array can me over written
print(a)
b = np.array([[1, 2, 3], [4, 5, 6]]) # Creating a 2D array i.e 2d-matrix
print(b.shape)
print(b[0,1], b[1, 2])

''' Functions to create arrays'''

a = np.zeros((3, 2))
print(a)
b = np.ones((5, 4))
print(b)
c= np.full((2, 5), 7) # Creates a constant array of elements
print(c)
d = np.eye(5)
print(d)
e = np.random.random((2,3)) # Creates an array filled with random elements
print(e)

''' Array indexing and slicing '''
a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(a)
b = a[:2, :3]
print(b)
print(a[0, 3])
row_1 = a[0, :] # Creates a rank 1 matrix -- this in tern becomes a collumn matrix
print(row_1, row_1.shape)
row_2 = a[1:2, :] # Creates a rank 2 matrix
print(row_2, row_2.shape)
col_1 = a[:, 2]
print(col_1, col_1.shape)
col_2 = a[:, 2:3]
print(col_2, col_2.shape)
print(a[[0, 1, 2], [1, 2, 3]]) # Ineger array indexing
print(a[0, 1], a[1, 2], a[2, 3]) # The above example is equivalent to this
c = np.arange(4) # creates an array from 0 to 4
print(c)
d = [0, 3, 2]
print(a[np.arange(3), d])
print(a[0, 0], a[1, 3], a[2, 2]) # The above example is equivalent to this
a[np.arange(3), d] += 10
print(a)

''' Boolean array indexing '''
bool_idx = a > 2 # Finds the elements of a > 2
print(bool_idx)
print(a[bool_idx]) # prints elemensts of a corresponding to True
print(a[a>2])

print(a.dtype) # Prints the dtype of a 
x = np.array([1, 2], dtype = np.float64) # Force a perticular datatype
print(x.dtype)

x = np.array([[1, 2], [3, 4]], dtype = np.float64)
y = np.array([[5, 6], [7, 8]])
print(x + y)
print(np.add(x, y))
print(x- y)
print(np.subtract(x, y))
print(x * y)
print(np.multiply(x, y))
print(x / y)
print(np.divide(x, y))
print(np.sqrt(x))

v = np.array([9, 10])
w = np.array([11, 12])

print(v.dot(w)) # Inner product of vectors (vector and a vector)
print(np.dot(v, w))

print(x.dot(v)) # Inner product of a matrix and a vector
print(np.dot(x, v))

print(x.dot(y)) # Elementwise multiplication
print(np.dot(x, y))

print(np.sum(a)) # Prints the sum of all the elements
print(np.sum(a, axis=0)) # sum along columns
print(np.sum(a, axis=1)) # sum along roms

print(a.T) # Transpose of the matrix
print(v.T) # Transpose of the vector


''' Broadcasting operation on arrays of different sizes '''
a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
v = np.array([1, 0 , -1, 0])
y = np.empty_like(a) # creates an empty array of size equal to x
for i in range(3):
    y[i, :] = a[i, :] + v # Columns of a and v must be same
print(y)

# -----or-------
vv = np.tile(v, (3,1)) # Stack 3 copies of v on top of each other
print(v)
y = a + v
print(y)
#-----or----
y = a + v # can also do the same as above without stacking the matrices
print(y)

  



