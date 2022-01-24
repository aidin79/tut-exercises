import cv2 as cv

image = cv.imread('test.jpeg')

flower = image[80:380, 280:580]

# print(cv.IMREAD_COLOR)
cv.imshow('image', image)
cv.waitKey(0)
cv.destroyAllWindows()

cv.imshow('flower', flower)
cv.waitKey(0)
cv.destroyAllWindows()

image[80:380, 680:980] = flower

cv.imshow('image', image)
cv.waitKey(0)
cv.destroyAllWindows()