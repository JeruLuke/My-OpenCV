import cv2
import numpy as np

def nothing(x):
    pass

img = cv2.imread('C:/Users/selwyn77/Desktop/Stack/ch.jpg', 0)
# Create a black image, a window
#img = np.zeros((300,512,3), np.uint8)
cv2.namedWindow('thresh1')

# create trackbars for color change
cv2.createTrackbar('R','thresh1', 0, 255, nothing)
#cv2.createTrackbar('G','image',0,255,nothing)
#cv2.createTrackbar('B','image',0,255,nothing)

# create switch for ON/OFF functionality
#switch = '0 : OFF \n1 : ON'
#cv2.createTrackbar(switch, 'image',0,1,nothing)

while(1):
#    cv2.imshow('image',img)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

    # get current positions of four trackbars
    r = cv2.getTrackbarPos('R','thresh1')
#    g = cv2.getTrackbarPos('G','image')
#    b = cv2.getTrackbarPos('B','image')
#    s = cv2.getTrackbarPos(switch,'image')
    ret,thresh1 = cv2.threshold(img, r, 255,cv2.THRESH_BINARY_INV)
    cv2.imshow('thresh1', thresh1)
#    if s == 0:
#        img[:] = 0
#    else:
#        img[:] = [b,g,r]

cv2.destroyAllWindows()


import cv2
import numpy as np
from matplotlib import pyplot as plt

def nothing(x):
  pass

mode = True
cv2.namedWindow('Colorbars')
hh='Max'
hl='Min'
wnd = 'Colorbars'
cv2.createTrackbar("Max", "Colorbars",0,255,nothing)
cv2.createTrackbar("Min", "Colorbars",0,255,nothing)
img = cv2.imread('C:/Users/selwyn77/Desktop/Stack/trackbar/ch.jpg',0)
img = cv2.resize(img, (0,0), fx=0.15, fy=0.15)
# titles = ['Original Image','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']
# images = [img, thresh1, thresh2, thresh3, thresh4, thresh5]
# for i in xrange(6):
#     plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
#     plt.title(titles[i])
#     plt.xticks([]),plt.yticks([])
# plt.show()
while(1):
   hul=cv2.getTrackbarPos("Max", "Colorbars")
   huh=cv2.getTrackbarPos("Min", "Colorbars")
   ret,thresh1 = cv2.threshold(img,hul,huh,cv2.THRESH_BINARY)
   ret,thresh2 = cv2.threshold(img,hul,huh,cv2.THRESH_BINARY_INV)
   ret,thresh3 = cv2.threshold(img,hul,huh,cv2.THRESH_TRUNC)
   ret,thresh4 = cv2.threshold(img,hul,huh,cv2.THRESH_TOZERO)
   ret,thresh5 = cv2.threshold(img,hul,huh,cv2.THRESH_TOZERO_INV)
   # cv2.imshow(wnd)
   cv2.imshow("thresh1",thresh1)
   cv2.imshow("thresh2",thresh2)
   cv2.imshow("thresh3",thresh3)
   cv2.imshow("thresh4",thresh4)
   cv2.imshow("thresh5",thresh5)
   k = cv2.waitKey(1) & 0xFF
   if k == ord('m'):
     mode = not mode
   elif k == 27:
     break
cv2.destroyAllWindows()


