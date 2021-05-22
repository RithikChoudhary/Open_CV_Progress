import cv2
import numpy as np

from utils.colors import color_dict_HSV

from buttons import Button

cap = cv2.VideoCapture(0)

cv2.namedWindow("frame")

LOWER, UPPER    = 1, 0
HSV             = color_dict_HSV['white']
ret             = False

color_buttons   = [
    Button(
        "red1",                 # Button Text
        10,30 ,                 # Button Position ( Top Left )
        textcolor=(0, 0, 255),
        scale=.8
    ),
    Button(
        "white",                 # Button Text
        80, 30,                 # Button Position ( Top Left )
        textcolor= (180, 180, 180),
        scale=.8
    ),
    Button(
        "green",                 # Button Text
        164, 30,                 # Button Position ( Top Left )
        textcolor= (0, 255, 0),
        scale=.8
    ),
    Button(
        "yellow",                 # Button Text
        256, 30,                 # Button Position ( Top Left )
        textcolor= (0, 180, 180),
        scale=.8
    )
]

while not ret:
    ret, init_frame = cap.read()
    
def click_mouse(event,x,y,flags,params):
    global HSV
    if event == 1:
        for btn in color_buttons:
            if btn.isInside(x,y):
                HSV = color_dict_HSV.get(btn.text)
                print("    selected :",(btn.text, HSV))
    return

cv2.setMouseCallback('frame',click_mouse)

def invisible():
    while cap.isOpened():
        _,frame = cap.read()

        hsv  = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV) 
        mask = cv2.inRange(hsv,HSV[LOWER], HSV[UPPER])
        
        frame[np.where(mask==255)]=init_frame[np.where(mask==255)]

        for btn in color_buttons:
            btn.show(frame)
        
        cv2.imshow('frame',frame)
        # cv2.imshow('mask',mask)

        if cv2.waitKey(1) == 27: break


invisible()

cap.release()
cv2.destroyAllWindows()
