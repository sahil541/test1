import cv2
import numpy as np
img = cv2.imread('./Image/walpaper.jpg')
def imagerotation(img,angle):
    height,width = img.shape[:2]
    rotation_matrix = cv2.getRotationMatrix2D((width/2,height/2),angle,1)
    dst = cv2.warpAffine(img,rotation_matrix,(width,height))
    return dst

rotation_img = imagerotation(img,45)
cv2.imshow('image',rotation_img)
cv2.waitKey(0)
cv2.destroyAllWindows()