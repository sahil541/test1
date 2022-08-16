import cv2
import numpy as np
img = cv2.imread('./image/walpaper.jpg')

pts = np.array([[10, 360], [45,260], [100, 360]],np.int32)
pts = pts.reshape(-1,1,2)

cv2.line(img, (20, 160), (100, 160), (0, 0, 255), 10)
cv2.rectangle(img, (200, 160), (400, 300), (0, 255, 0), 2)
cv2.circle(img, (600, 160), 100, (255, 0, 0), 2)
cv2.ellipse(img, (900, 160), (100, 50), 0, 0, 360, (255, 0, 255), 2)
cv2.polylines(img, [pts], True, (255, 0, 0), 2)
cv2.fillConvexPoly(img, pts,(0, 0, 255))
cv2.arrowedLine(img, (10, 460), (100, 460), (255, 0, 255), 3)
cv2.putText(img, 'OpenCV', (200, 460), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
