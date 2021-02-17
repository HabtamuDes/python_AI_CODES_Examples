import cv2
import numpy as np


img = cv2.imread('face_1.jpg')

# get image height, width
(h, w) = img.shape[:2]
# calculate the center of the image
center = (w / 2, h / 2)

angle90 = 90

scale = 1.0

# Perform the counter clockwise rotation holding at the center
# 90 degrees

M = cv2.getRotationMatrix2D(center, angle90, scale)

rotated90 = cv2.warpAffine(img, M, (h, w))

cv2.imshow('rotated_image',rotated90)
cv2.waitKey(0)

cv2.destroyAllWindows()


