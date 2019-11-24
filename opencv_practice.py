# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 23:51:42 2019

@author: Rohan
"""
''' OpenCV practice '''

import numpy as np
import matplotlib.pyplot as plt
import cv2
import random

''' -------------------- '''

img = cv2.imread('Lena_headey_.png')
print(type(img))
print('Original Image shape:', img.shape)
print('Image dtype:', img.dtype)
resized_img = cv2.resize(img, (800, 400))
print('Resized image size is:', resized_img.shape)
resized_img = cv2.resize(img, (0, 0), resized_img, 0.5, 0.3)
print('Resized image size is:', resized_img.shape)

img_flip_along_x = cv2.flip(img, 0) # Flip along horizontal axis
img_flip_along_y = cv2.flip(img, 1) # Flip along vertical axis
img_flip_xy = cv2.flip(img, -1) # Flip both hori and verti

cv2.imwrite('Lena_headey_edited.png', img [cv2.IMWRITE_PNG_COMPRESSION, 0]) # To save images

cv2.imshow('Image', img)
cv2.waitKey(2000)

''' Named Window '''
cv2.namedWindow('Window')
print(dir(cv2))
fill_val = np.array([255, 255, 255], np.unit8)

def trackbar _callback(idx, value):
    fill_val[idx] = value

cv2.createTrackbar('R', 'Window', 255, 255, lambda v: trackbar_callback(2, v))

while True:
    image = np.full((500, 500, 3), fill_val)
    cv2.imshow('Window', image)
    key = cv2.waitKey(3)
    if key == 27:
        break
cv2.destroyAllWindows()


''' ----------  lines markers ellipse--------------'''
img = cv2.resize(img, (800, 350))

cv2.circle(img, (100, 50), 40, (255, 0, 0))
cv2.circle(img, (80, 20), 60, (0, 250, 0), cv2.FILLED)

cv2.imshow('Image', img)
cv2.waitKey(200)

cv2.line(img, 50, 250, (85, 255, 20), 2)
cv2.line(img, 50, 250, (85, 25, 100), 3, cv2.LINE_AA)
cv2.arrowedLine(img, 80, 99, (255, 255, 0), 3, cv2.LINE_AA)
cv2.putText(img, 'OpenCV', (50, 60), cv2.FONT_HERSHEY_SIMPLEX)

''' To capture live video '''
cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    if not frame:
        break
    
    cv2.imshow('video', frame)
    key = cv2.waitKey()
    if key == 27:
        break
cap.release()
cv2.destroyAllWindow()

''' Time and Date '''
cap = cv2.VideoCapture(0)
print(cv2.get(3))
print(cv2.get(4))

while (cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        font = cv2.FONT_HERSHEY_SIMPLEX
        text = 'Width:' + str(cap.get(3)) + 'Height:' + str(cap.get(4))
        frame = cv2.putText(frame, text, (10, 50), font, 5, (0, 0, 255), cv2.Line_AA)
        date = str(datetime.datetime.now())
        frame = cv2.putText(frame, date, (10, 50), font, 5, (0, 0, 255), cv2.Line_AA)
cap.release()
cv2.destroyAllWindows()
''' Arithmetic operation on images'''


img = cv2.imread('Bar_graph.png')
img2 = cv2.imread('Lena_headey_.png')
print(img.shape)
print(img2.shape)
b, g, r = cv2.split(img2)
img = cv2.merge((b, g, r))

ball = img[280:340, 330:390]
# img[200:336, 100:160] = ball

img = cv2.resize(img, (512, 512))
img2 = cv2.resize(img2, (512, 512))
dst = cv2.add(img, img2)
dst = cv2.addWeighted(img, 0.9, img2, 0.1, 0)
cv2.imshow('image', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()


