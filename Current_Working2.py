import cv2
import numpy as np
import imutils
cap = cv2.VideoCapture(0)

while cap.isOpened():
    _,frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_RGB2HSV)
    lower = np.array([0, 10, 60], dtype = "uint8") 
    upper = np.array([20, 150, 255], dtype = "uint8")
    mask = cv2.inRange(hsv,lower,upper)
    
    cnt = cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    # print(*cnt)
    cnt = imutils.grab_contours(cnt)
    for c in cnt:
        area = cv2.contourArea(c)
        cv2.drawContours(frame,[c],-1,(0,255,0),3)
        M = cv2.moments(c)
        # cx = int(M["m10"]/ M["m00"])
        # cy = int(M["m01"]/M["m00"])
        
        cv2.circle(frame,(50,50),7,(255,255,0),-1)
        
    
    cv2.imshow("frame",frame)
    key = cv2.waitKey(1)
    if key == 27:
        break
cap.release()
cv2.destroyAllWindows()
