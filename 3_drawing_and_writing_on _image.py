import cv2 as cv
import numpy as np

image = cv.imread('test.jpeg')

cv.line(image, (0,0), (100, 100), (0, 0, 255), thickness=2)
cv.imshow('test', image)
cv.waitKey(0)
cv.destroyAllWindows()

cv.circle(image, (900, 500), 50, (100, 120, 0), thickness=4)
cv.imshow('test', image)
cv.waitKey(0)
cv.destroyAllWindows()

cv.rectangle(image, (0,0), (100, 100), (200, 200, 200), thickness=2)
cv.imshow('test', image)
cv.waitKey(0)
cv.destroyAllWindows()

pts = np.array([[0,0], [100,0], [200,100], [100,200], [0, 100]])
cv.polylines(image, [pts], True, (50,150,100), thickness=10)
cv.imshow('test', image)
cv.waitKey(0)
cv.destroyAllWindows()