'''
Find contours in an image and store their coordinates for each corresponding contour in a separate file 
'''

import numpy as np
import cv2

THRESHOLD = 55

path = 'C:/Users/selwyn77/Desktop/Stack/contour/'
im = cv2.imread(path + 'date.jpg')
imgray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
cv2.imshow("imgray", imgray)

ret, thresh = cv2.threshold(imgray, THRESHOLD, 255, 0)
cv2.imshow('thresh', thresh)

_th, contours, hierarchy = cv2.findContours(cv2.bitwise_not(thresh), cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
print "Number of contours detected = %d" % len(contours)

cv2.drawContours(im, contours, -1, (1, 70, 255), 2)
cv2.imshow("Contours", im)
 
contour_num = 0 
for i in range(0, len(contours)):
    coords = np.array2string(contours[i])
    contour_num+=1
    open(path + 'contour_%d.txt' %contour_num, "w").write(coords)
    
cv2.waitKey(0)
cv2.destroyAllWindows()