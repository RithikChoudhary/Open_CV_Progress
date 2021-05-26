import cv2
import numpy as np

# cap = cv2.VideoCapture(0)
img1 = cv2.imread("D:\Code\python\AI\img1.jpeg")
img2 = cv2.imread("D:\Code\python\AI\img2.jpeg")
# img1 = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
# img2 = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
# bit = cv2.bitwise_and(img1,img2,mask=None)
hsv1 = cv2.cvtColor(img1,cv2.COLOR_BGR2HSV)
hsv2 = cv2.cvtColor(img2,cv2.COLOR_BGR2HSV)
small1 = img1.min(axis=(0,1))
large1 = img1.max(axis=(0,1))
small2 = img2.min(axis=(0,1))
large2 = img2.max(axis=(0,1))
mask1 = cv2.inRange(hsv1,small1,large1)
mask2 = cv2.inRange(hsv2,small2,large2)
mask = mask1+mask2

edge = cv2.Canny(mask,100,200)
# mask = cv2.cvtColor(mask,cv2.COLOR_GRAY2BGR)
cv2.imshow("frame",edge)

# cv2.imshow("frame",bit)
cv2.imshow("img1",img1)
cv2.imshow("img2",img2)
if cv2.waitKey(0) & 0xff == 27: 
    cv2.destroyAllWindows() 
