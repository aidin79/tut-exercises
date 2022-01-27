import cv2 as cv
import numpy as np
from helpers import Helpers

helpers = Helpers()

image = cv.imread('utd.jpg')

res = helpers.color_filter(image, [30,150,50], [255,255,230])

cv.imshow('image', image)
cv.waitKey(0)
cv.destroyAllWindows()

cv.imshow('res', res)
cv.waitKey(0)
cv.destroyAllWindows()

kernel = np.ones((15,15), np.float32) / 255
smoothed = cv.filter2D(res, -1, kernel)
cv.imshow('smoothed', smoothed)
cv.waitKey(0)
cv.destroyAllWindows()

gaussian_blur = cv.GaussianBlur(res, (15,15), 0)
cv.imshow('gaussian_blur', gaussian_blur)
cv.waitKey(0)
cv.destroyAllWindows()

median_blur = cv.medianBlur(res, 15)
cv.imshow('median_blur', median_blur)
cv.waitKey(0)
cv.destroyAllWindows()

bilateral_filter = cv.bilateralFilter(res, 15, 75, 75)
cv.imshow('bilateral_filter', bilateral_filter)
cv.waitKey(0)
cv.destroyAllWindows()