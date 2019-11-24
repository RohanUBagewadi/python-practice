# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 12:47:19 2019

@author: Rohan
"""

''' SciPY library practice '''

import imageio
from imageio import imsave
print(dir(imageio))
img = imageio.imread('Bar_graph.png')
print(img.dtype, img.shape)
imsave('Bar_graph1.png', img)

# Distance between points
import numpy as np
from scipy.spatial.distance import pdist, squareform
x = np.array([[0, 1], [1, 0], [2, 0]])
d = squareform(pdist(x, 'euclidean')) # Computes the euclidean distance between all the rows of x
print(d) # d[i, j] is the euclidean distance between x[i,:] and x[j,:]
