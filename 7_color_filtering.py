import cv2 as cv
import numpy as np

image = cv.imread('blue.jpeg')

hsv = cv.cvtColor(image, cv.COLOR_BGR2HSV)

lower_blue = np.array([60, 35, 140])
upper_blue = np.array([180, 255, 255])

mask = cv.inRange(hsv, lower_blue, upper_blue)
res = cv.bitwise_and(image,image, mask= mask)

cv.imshow('image', image)
cv.waitKey(0)
cv.destroyAllWindows()

cv.imshow('flower', res)
cv.waitKey(0)
cv.destroyAllWindows()