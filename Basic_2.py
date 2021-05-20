import cv2
import numpy as np

def nothing():
    pass
cap = cv2.VideoCapture(0)
while True:
    cv2.waitKey(1000)
    global init_frame
    ret,init_frame = cap.read()
    if ret==True:
        break
    
def click_mouse(event,x,y,flag,param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        if (x,y) in ((5,60),(60,20)):
            lower_hsv = np.array([90,50,70])
            upper_hsv = np.array([128,255,255])
            return lower_hsv,upper_hsv
    lower_hsv = np.array([0,0,0])
    upper_hsv = np.array([0,0,0])        
    return lower_hsv,upper_hsv
    
    
def invisible():
    while cap.isOpened():
        _,frame = cap.read()
        hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
        lower_hsv = np.array([90,50,70])
        upper_hsv = np.array([128,255,255])
        
        lower_hsv,upper_hsv=click_mouse()
        
        mask = cv2.inRange(hsv,lower_hsv,upper_hsv)
        
        frame[np.where(mask==255)]=init_frame[np.where(mask==255)]
        cv2.rectangle(frame,(5,60),(60,20),(255,255,255),-1,cv2.LINE_AA)
        # cv2.rectangle(frame,(140,60),(60,20),(255,0,255),-1,cv2.LINE_AA)
        # cv2.rectangle(frame,(210,60),(140,20),(0,0,255),-1,cv2.LINE_AA)
        # print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        # print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        
        cv2.putText(frame,"Red",(20,50),cv2.FONT_HERSHEY_COMPLEX,.5,(0,0,255),2,cv2.LINE_AA)
        
        # cv2.putText(frame,"Green",(80,50),cv2.FONT_HERSHEY_COMPLEX,.5,(0,255,0),2,cv2.LINE_AA)
        # cv2.putText(frame,"Yellow",(150,50),cv2.FONT_HERSHEY_COMPLEX,.5,(25,255,255),2,cv2.LINE_AA)
        # cv2.putText(frame,"Blue",(240,50),cv2.FONT_HERSHEY_COMPLEX,.5,(255,255,105),2,cv2.LINE_AA)
        
        cv2.imshow('frame',frame)
        # cv2.imshow('mask',mask)

        k = cv2.waitKey(1)
        if k == 27:
            cap.release()
            break

invisible()
cv2.setMouseCallback('frame',click_mouse)
cap.release()
cv2.destroyAllWindows()
