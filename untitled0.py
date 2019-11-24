# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 18:12:33 2019

@author: Rohan
"""

import cv2
import numpy as np

img = cv2.imread('Bar_graph.png')
mouse_pressed = False
s_x = s_y = e_x = e_y = -1
def mouse_callback(event, x, y, flag, param):
    global img, s_x, s_y, e_x, e_y, mouse_pressed

    if event == cv2.EVENT_LBUTTONDOWN:
        mouse_pressed = True
        s_x, s_y = x, y
        img = np.copy(img)
    elif event == cv2.EVENT_MOUSEMOVE:
        if mouse_pressed:
            img = np.copy(img)
            cv2.rectangle(img, (s_x, s_y), (x, y), (0, 255, 255), 1)
    elif event == cv2.EVENT_LBUTTONUP:
        mouse_pressed = False
        e_x, e_y = x, y
cv2.namedWindow('Image')
cv2.setMouseCallback('img', mouse_callback)

while True:
    cv2.imshow('Image', img)
    k = cv2.waitKey(1)

    if k == ord('c'):
        if s_y > e_y:
            s_y, e_y = e_y, s_y
        if s_x > e_x:
            s_x, e_x = e_x, s_y
        if e_y - s_y > 1 and e_x - s_x >0:
            img = img[s_y:e_y, s_x:e_x]
    elif k==27:
        break
cv2.destroyAllWindows()