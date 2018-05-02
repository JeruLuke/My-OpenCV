#--- Script to find the contour with the greatest area ---

import cv2
import numpy as np

path = 'C:/Users/selwyn77/Desktop/Stack/rough/'
img = cv2.imread(path + 'car.jpg')
img = cv2.resize(img, (0,0), fx=0.25, fy=0.25)

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
h, s, v = cv2.split(hsv)

cv2.imshow('hsv Image', hsv)
cv2.imshow('h Image', h)
cv2.imshow('s Image', s)
cv2.imshow('v Image', v)

ret, thresh = cv2.threshold(s, 87, 255, cv2.THRESH_BINARY)
cv2.imshow('hue_thresh', thresh)


kernel1 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
dilation = cv2.dilate(cv2.bitwise_not(thresh), kernel1, iterations = 4)
cv2.imshow('dilation', dilation)

_, contours, hierarchy =    cv2.findContours(dilation, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
big_cnt = 0
max_area = 0

for cnt in contours:
    if (cv2.contourArea(cnt) > max_area):
        max_area = cv2.contourArea(cnt)
        big_cnt = cnt
        
x, y, w, h = cv2.boundingRect(big_cnt)
cv2.rectangle(img, (x,y), (x+w,y+h), (0, 255, 0), 2)
cv2.imshow('rect_img', img)

cv2.imwrite(path + 'rect_img.jpg', img)
        
cv2.waitKey(0)
cv2.destroyAllWindows()


