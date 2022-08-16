import cv2
import numpy as np
img = cv2.imread('./Image/walpaper.jpg')
def imagetranslation(img,x,y):
    M = np.float32([[1,0,x],[0,1,y]])
    dst = cv2.warpAffine(img,M,(img.shape[1],img.shape[0]))
    return dst
height,width = img.shape[:2]
translation_img = imagetranslation(img,width/4,height/4)
cv2.imwrite('./Image/translation.jpg',translation_img)