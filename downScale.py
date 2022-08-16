import cv2
import numpy as np
img = cv2.imread('./Image/walpaper.jpg')
def downscale(img,scale):
    height,width = img.shape[:2]
    scaled_height = int(height/scale)
    scaled_width = int(width/scale)
    scaled_img = cv2.resize(img,(scaled_width,scaled_height))
    return scaled_img
scaled_img = downscale(img,2)
cv2.imwrite('./Image/downScaled.jpg',scaled_img)