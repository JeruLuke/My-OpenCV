#--- Code to find contour regions and save them as separate images ---

import numpy as np
import cv2
import matplotlib.pyplot as plt
# This is font for labels
font = cv2.FONT_HERSHEY_SIMPLEX

path = 'C:/Users/selwyn77/Desktop/Stack/contour/'
im = cv2.imread(path + 'date.jpg')
imgray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)

ret2,th2 = cv2.threshold(imgray,0,255,cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
#cv2.imwrite(path + 'dateth2.jpg', th2)

im2 = im.copy()
_, contours, hierarchy = cv2.findContours(th2, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
count = 0
for cnt in contours:
#    if (cv2.contourArea(cnt) > 100):
        x, y, w, h = cv2.boundingRect(cnt)
#        cv2.rectangle(im2, (x,y), (x+w,y+h), (0, 255, 0), 2)
        crop_img = im2[y:y+h, x:x+w]
#        cv2.imwrite(path + 'date_' + str(count) + '_.jpg', crop_img)
        cv2.imshow(str(count), crop_img)
        count+=1
print('Number of probable characters', count) 

cv2.imshow(path + 'contoursdate.jpg', im2)
#cv2.imwrite(path + 'contoursdate.jpg', im2)

cv2.waitKey(0)
cv2.destroyAllWindows()