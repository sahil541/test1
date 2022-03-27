import cv2
image = cv2.imread("profile.jpg")
cv2.imwrite("copy.jpg", image)

height, width, channels = image.shape

print('Height: ' , height)
print('Width: ' , width)

print('Resolution: ', height*width)
