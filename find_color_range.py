import cv2
import numpy as np


u = np.uint8([[[0,236,236]]])
 # define range of blue color in HSV
lower_yellow = np.array(cv2.cvtColor(l,cv2.COLOR_BGR2HSV))
upper_yellow = np.array( cv2.cvtColor(u,cv2.COLOR_BGR2HSV))
print(lower_yellow)
print(upper_yellow)


color_dict_HSV = {'black': [[180, 255, 30], [0, 0, 0]],
              'white': [[180, 18, 255], [0, 0, 231]],
              'red1': [[180, 255, 255], [159, 50, 70]],
              'red2': [[9, 255, 255], [0, 50, 70]],
              'green': [[89, 255, 255], [36, 50, 70]],
              'blue': [[128, 255, 255], [90, 50, 70]],
              'yellow': [[35, 255, 255], [25, 50, 70]],
              'purple': [[158, 255, 255], [129, 50, 70]],
              'orange': [[24, 255, 255], [10, 50, 70]],
              'gray': [[180, 18, 230], [0, 0, 40]]}


