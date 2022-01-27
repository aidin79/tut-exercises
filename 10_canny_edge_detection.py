import cv2 as cv
from helpers import Helpers

helpers = Helpers()

image = cv.imread('utd.jpg')
cv.imshow('image', image)
cv.waitKey(0)
cv.destroyAllWindows()

res = helpers.color_filter(image, [30,150,50], [255,255,230])
cv.imshow('res', res)
cv.waitKey(0)
cv.destroyAllWindows()

laplacin = cv.Laplacian(res, cv.CV_64F)
cv.imshow('laplacin', laplacin)
cv.waitKey(0)
cv.destroyAllWindows()

sobel_x = cv.Sobel(res, cv.CV_64F, 1, 0, ksize=5)
cv.imshow('sobel_x', sobel_x)
cv.waitKey(0)
cv.destroyAllWindows()

sobel_y = cv.Sobel(res, cv.CV_64F, 0, 1, ksize=5)
cv.imshow('sobel_y', sobel_y)
cv.waitKey(0)
cv.destroyAllWindows()

edges = cv.Canny(image, 100, 250)
cv.imshow('edges', edges)
cv.waitKey(0)
cv.destroyAllWindows()