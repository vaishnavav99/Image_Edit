import numpy as np
import cv2

img=cv2.imread("test.jpg")

gray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gray= cv2.medianBlur(gray,3)
edges=cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,9,9)
color = cv2.bilateralFilter(img,19,250,250)
cartoon = cv2.bitwise_and(color,color,mask=edges)
cv2.imwrite("out.png",cartoon)
