'''
Script to rotate images clockwise and anti-clockwise using the mouse
'''


import cv2 as cv
#import numpy as np

DEF_ANGLE = 0
pressed_left = False
pressed_right = False

def click_to_rotate(event, x, y, flags, param):
    global DEF_ANGLE, DEF_ANGLE1, pressed_left, pressed_right
    
    if event == cv.EVENT_LBUTTONDOWN:
        pressed_left = True
        DEF_ANGLE += 1
        
    elif event == cv.EVENT_MOUSEMOVE:
        #print('x,y',x,y)
        if(pressed_left):
            DEF_ANGLE += 1 
            
    if event == cv.EVENT_RBUTTONDOWN:
        pressed_right = True
        DEF_ANGLE -= 1
        
    elif event == cv.EVENT_MOUSEMOVE:
        #print('x,y',x,y)
        if(pressed_right):
            DEF_ANGLE -= 1 
    
    elif event == cv.EVENT_LBUTTONUP:
        pressed_left = False
        
    elif event == cv.EVENT_RBUTTONUP:
        pressed_right = False
#        if event == cv.EVENT_MOUSEMOVE:
        #print('x,y',x,y)
#            if(pressed):
#                DEF_ANGLE += 1

cv.namedWindow('window')
path = 'C:/Users/selwyn77/Desktop/'
img = cv.imread(path + 'ch.jpg')
img = cv2.resize(img, (0, 0), fx = 0.1, fy = 0.1) 
cv.setMouseCallback('window', click_to_rotate)

while(True):
    num_rows, num_cols = img.shape[:2]
    rotation_matrix = cv.getRotationMatrix2D((num_cols/2, num_rows/2), DEF_ANGLE, 1)
    img_rotation = cv.warpAffine(img, rotation_matrix, (num_cols, num_rows))
    cv.imshow('window', img_rotation)
    k = cv.waitKey(1) & 0xFF
    if k == 27:
        break

cv.destroyAllWindows()