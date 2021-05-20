# Be the Mr.India only in Blue Color


import cv2
import numpy as np

cap = cv2.VideoCapture(0)
while True:
    cv2.waitKey(1000)
    global init_frame
    ret,init_frame = cap.read()
    if ret==True:
        break
def invisible():
    while cap.isOpened():
        _,frame = cap.read()
        hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
        lower_hsv = np.array([90,50,70])
        upper_hsv = np.array([128,255,255])
        mask = cv2.inRange(hsv,lower_hsv,upper_hsv)
        
        frame[np.where(mask==255)]=init_frame[np.where(mask==255)]
        
        cv2.imshow('frame',frame)
        cv2.imshow('mask',mask)

        k = cv2.waitKey(1)
        if k == 27:
            cap.release()
            break

invisible()
cap.release()
cv2.destroyAllWindows()
