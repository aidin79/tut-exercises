import cv2 as cv
import numpy as np
from helpers import Helpers
helpers = Helpers()

image = cv.imread('blue.jpeg')

res = helpers.color_filter(image, [60, 35, 140], [180, 255, 255])

cv.imshow('image', image)
cv.waitKey(0)
cv.destroyAllWindows()

cv.imshow('flower', res)
cv.waitKey(0)
cv.destroyAllWindows()