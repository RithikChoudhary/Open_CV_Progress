import cv2
import numpy as np

cap = cv2.VideoCapture(0)
cv2.namedWindow("frame")
LOWER, UPPER = 1, 0

color_dict_HSV = {
    'black'     : [np.array([180, 255, 30]), np.array([0, 0, 0])],
    'white'     : [[180, 18, 255], [0, 0, 231]],
    'red1'      : [np.array([180, 255, 255]), np.array([159, 50, 70])],
    'red2'      : [[9, 255, 255], [0, 50, 70]],
    'green'     : [np.array([89, 255, 255]), np.array([36, 50, 70])],
    'blue'      : [[128, 255, 255], [90, 50, 70]],
    'yellow'    : [[35, 255, 255], [25, 50, 70]],
    'purple'    : [[158, 255, 255], [129, 50, 70]],
    'orange'    : [[24, 255, 255], [10, 50, 70]],
    'gray'      : [np.array([180, 18, 230]), np.array([0, 0, 40])]
}

# (BL, TR)
'''
    (XL, YT)
             +-------------------+
             |                   |
             |       R E D       |
             |                   |
             +-------------------+ 
                                   (XR, YB)
 RED BOX = Dimestions = (50, 30)                                   
'''
color_button_pos = {
    #               XL    YT   XR     YB
    'red1'      : ([10  , 30],[60  ,  60]),
}

HSV = color_dict_HSV['green']

while True:
    cv2.waitKey(1000)
    global init_frame
    ret,init_frame = cap.read()
    if ret==True:
        break
    
def click_mouse(event,x,y,flags,params):
    global HSV
    if event == 1:
        # this line will print the current BGR value of the frame after the mouse click
        colors = frame[y,x]
        print(str(colors) +"    \n\n" )
        print(x,y)
        
        # if [x,y] in color_button_pos['red1']:
        (x_left, y_top), (x_right, y_bottom) = color_button_pos['red1']
        if x in range(x_left, x_right) and y in range(y_top, y_bottom):
            HSV = color_dict_HSV['red1']
#             print(HSV)
            return         
        
        print(HSV)

    return

cv2.setMouseCallback('frame',click_mouse)

def invisible():
    global frame
    while cap.isOpened():
        _,frame = cap.read()
        hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
        # lower_hsv = np.array([90,50,70])
        # upper_hsv = np.array([128,255,255])
    
         
        mask = cv2.inRange(hsv,HSV[LOWER], HSV[UPPER])
        
        frame[np.where(mask==255)]=init_frame[np.where(mask==255)]
        
        (x_left, y_top), (x_right, y_bottom) = color_button_pos['red1']
        cv2.rectangle(frame,(x_left,y_top),(x_right,y_bottom),(255,255,255),-1,cv2.LINE_4)
        
        # cv2.rectangle(frame,(140,60),(60,20),(255,0,255),-1,cv2.LINE_AA)
        # cv2.rectangle(frame,(210,60),(140,20),(0,0,255),-1,cv2.LINE_AA)
        # print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        # print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        
        
        cv2.putText(frame,"Oil",(x_left,y_top+20),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,255),1,cv2.LINE_AA)
        # cv2.putText(frame,"Red",(20,50),cv2.FONT_HERSHEY_COMPLEX,.5,(0,0,255),2,cv2.LINE_8)
        # cv2.putText(frame,"Red",(20,50),cv2.FONT_HERSHEY_COMPLEX,.5,(0,0,255),2,cv2.LINE_AA)
        
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

cap.release()
cv2.destroyAllWindows()
