import numpy as np
import cv2
from skimage import data,filters
cap=cv2.VideoCapture('input.mp4')
frameids=cap.get(cv2.CAP_PROP_FRAME_COUNT)*np.random.uniform(size=25)
frames=[]
for i in frameids:
    cap.set(cv2.CAP_PROP_POS_FRAMES,i)
    ret,frame=cap.read()
    frames.append(frame)
medianFrame=np.median(frames,axis=0).astype(dtype=np.uint8)
cv2.imshow('frame',medianFrame)
cv2.waitKey(0)