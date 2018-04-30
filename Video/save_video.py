import numpy as np
import cv2

cap = cv2.VideoCapture(0)


out = cv2.VideoWriter('output.avi',-1, 20.0, (640,480))

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret:
        gray = cv2.cvtColor(src=frame, code=cv2.COLOR_BGR2GRAY)

        out.write(gray)

        cv2.imshow('frame', gray)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
out.release()
cv2.destroyAllWindows()