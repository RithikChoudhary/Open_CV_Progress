import cv2
import numpy as np
import mediapipe as mp


mphands = mp.solutions.hands
hand = mphands.Hands()
mpDraw = mp.solutions.drawing_utils
cap = cv2.VideoCapture(0)

while cap.isOpened():
    _,frame = cap.read()
    
    converted = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    result = hand.process(converted)
    
    if result.multi_hand_landmarks:
        for hand_in_frame in result.multi_hand_landmarks:
            mpDraw.draw_landmarks(frame,hand_in_frame,mphands.HAND_CONNECTIONS)
             
    cv2.imshow("frame",frame)
    key = cv2.waitKey(1)
    if key == 27:
        break
    
cap.release()
cv2.destroyAllWindows()
