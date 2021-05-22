import cv2
import numpy as np

cap = cv2.VideoCapture(0)
def Motion_Detection():
    
    while True:
    
        _,frame1 = cap.read()            #getting first frame
        _,frame2 = cap.read()            #getting second frame
        sub = cv2.absdiff(frame1,frame2) #Taking the diffrence of the frames so that camera only detect the diffrence of motion in both frames
                                                                                    
        gray = cv2.cvtColor(sub,cv2.COLOR_BGR2GRAY)
        edge = cv2.Canny(gray,100,255)                                      # Detecting the edges for drawing contours
        
        cont,_ = cv2.findContours(edge,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE) # Finding the contours of the edges detected in the sub
        
        if cont:                                                            # if contours detected then it try to draw rectangle around it
            contr = max(cont,key=cv2.contourArea)
            (x,y,w,z) = cv2.boundingRect(contr)
            # if cv2.contourArea(cont) < 100:
            #    continue
                   
            cv2.rectangle(frame1,(x,y),(x+w,y+z),(0,0,255),3,cv2.LINE_AA)
            cv2.drawContours(frame1,cont,-1,(0,255,0),3)
            
        cv2.imshow("Motion",frame1)
        key = cv2.waitKey(1)
        if key ==27:
            break
Motion_Detection()    
cap.release()
cv2.destroyAllWindows()
