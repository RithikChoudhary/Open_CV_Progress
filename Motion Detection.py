import cv2
import numpy as np

cap = cv2.VideoCapture(0)
while True:
 
    _,frame = cap.read()
    _,frame1 = cap.read()
    sub = cv2.absdiff(frame,frame1)
    
    gray = cv2.cvtColor(sub,cv2.COLOR_BGR2GRAY)
    edge = cv2.Canny(gray,100,255)
    
    cnt,_ = cv2.findContours(edge,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
    
    # for cont in cnt:
    #     (x,y,w,z) = cv2.boundingRect(cont)
        
    #     if cv2.contourArea(cont) < 100:
    #         continue
    #     # area = cv2.contourArea(cont)
    #     else:
    #         cv2.rectangle(frame,(x,y),(x+w,y+z),(0,0,255),3,cv2.LINE_AA)
        
    
    cv2.drawContours(frame,cnt,-1,(0,255,0),3)
    cv2.imshow("sub",frame)
    
    key = cv2.waitKey(1)
    if key ==27:
        break
    
cap.release()
cv2.destroyAllWindows()
