import cv2
import numpy as np


img = cv2.imread('face_1.jpg')

x = 0
y = 0

width = 100
height = 100

cropped_img = img[y:y+height, x:x+width]

cv2.imshow("cropped_images", cropped_img)
cv2.waitKey(0)
cv2.destroyAllWindows()