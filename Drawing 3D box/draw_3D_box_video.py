'''
Draw 3D box around a square while streaming a video
'''

import cv2
import numpy as np
import imutils

cap = cv2.VideoCapture(0)

while True:

    try:
        ret, image = cap.read()

        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (5, 5), 0)
        thresh = cv2.threshold(gray, 190, 255, cv2.THRESH_BINARY)[1]
        #cv2.bitwise_not(thresh, thresh)

        cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
                cv2.CHAIN_APPROX_SIMPLE)
        cnts = cnts[0] if imutils.is_cv2() else cnts[1]
        c = max(cnts, key=cv2.contourArea)

        rect = cv2.minAreaRect(c)
        angle = rect[2]


        extLeft = tuple(c[c[:, :, 0].argmin()][0])
        extRight = tuple(c[c[:, :, 0].argmax()][0])
        extTop = tuple(c[c[:, :, 1].argmin()][0])
        extBot = tuple(c[c[:, :, 1].argmax()][0])

        if angle < 0:

            leftx = int(extLeft[0]) - int(angle)
            lefty = int(extLeft[1]) - 50 + int(angle)

            rightx = int(extRight[0]) - int(angle)
            righty = int(extRight[1]) -50 + int(angle)

            topx = int(extTop[0]) - int(angle)
            topy = int(extTop[1]) -50 + int(angle) 

            bottomx = int(extBot[0]) - int(angle)
            bottomy = int(extBot[1]) -50 + int(angle)

            leftc = (leftx, lefty)
            rightc = (rightx, righty)
            topc = (topx, topy)
            bottomc = (bottomx, bottomy)

            line = cv2.line(image, extLeft, leftc, (0,255,0), 2)
            line = cv2.line(image, extRight, rightc, (0,255,0), 2)
            line = cv2.line(image, extTop, topc, (0,255,0), 2)
            line = cv2.line(image, extBot, bottomc, (0,255,0), 2)
            line = cv2.line(image, bottomc, leftc, (0,255,0), 2)
            line = cv2.line(image, rightc, topc, (0,255,0), 2)
            line = cv2.line(image, leftc, topc, (0,255,0), 2)
            line = cv2.line(image, rightc, topc, (0,255,0), 2)
            line = cv2.line(image, bottomc, rightc, (0,255,0), 2)
            cv2.drawContours(image, [c], -1, (0,255,0), 2)

        elif angle > 0:

            leftx = int(extLeft[0]) + int(angle)
            lefty = int(extLeft[1]) + 50 + int(angle)

            rightx = int(extRight[0]) + int(angle)
            righty = int(extRight[1]) +50 + int(angle)

            topx = int(extTop[0]) + int(angle)
            topy = int(extTop[1]) +50 + int(angle) 

            bottomx = int(extBot[0]) + int(angle)
            bottomy = int(extBot[1]) +50 + int(angle)

            leftc = (leftx, lefty)
            rightc = (rightx, righty)
            topc = (topx, topy)
            bottomc = (bottomx, bottomy)

            line = cv2.line(image, extLeft, leftc, (0,255,0), 2)
            line = cv2.line(image, extRight, rightc, (0,255,0), 2)
            line = cv2.line(image, extTop, topc, (0,255,0), 2)
            line = cv2.line(image, extBot, bottomc, (0,255,0), 2)
            line = cv2.line(image, bottomc, leftc, (0,255,0), 2)
            line = cv2.line(image, rightc, topc, (0,255,0), 2)
            line = cv2.line(image, leftc, topc, (0,255,0), 2)
            line = cv2.line(image, rightc, topc, (0,255,0), 2)
            line = cv2.line(image, bottomc, rightc, (0,255,0), 2)
            cv2.drawContours(image, [c], -1, (0,255,0), 2)

    except:
        pass

    cv2.imshow("Image", image)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break