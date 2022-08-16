import cv2
import numpy as np
img = cv2.imread('./Image/walpaper.jpg')
def upScale(img,scale):
    height,width = img.shape[:2]
    scaled_height = int(height*scale)
    scaled_width = int(width*scale)
    scaled_img = cv2.resize(img,(scaled_width,scaled_height))
    return scaled_img
scaled_img = upScale(img,2)
cv2.imwrite('upScaled.jpg',scaled_img)