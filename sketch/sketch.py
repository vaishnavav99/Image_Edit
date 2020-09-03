import numpy as np
import cv2
import imageio
import scipy.ndimage

img='test.jpg'
def dodge(front,back):
    result = front*255/(260 - back)
    result[result>255]=255
    result[back==255]=255
    return result.astype('uint8')

i=imageio.imread(img)
gray=np.dot(i[...,:3],[0.299,0.587,0.114])
s=255-gray
b=scipy.ndimage.filters.gaussian_filter(s,sigma=100)
r=dodge(b,gray)
cv2.imwrite('out.png',r)
    
