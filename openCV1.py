import cv2
import numpy as np
'''  '''
img = cv2.imread('Bar_graph.png')
img2 = cv2.imread('Lena_headey_.png')
print(img.shape)
print(img2.shape)




cv2.imshow('image', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()