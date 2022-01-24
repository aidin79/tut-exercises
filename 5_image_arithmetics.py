import cv2 as cv

image = cv.imread('test.jpeg')
logo = cv.imread('phoenix.jpg')
logo = cv.resize(logo, (108,108))

cv.imshow('image', image)
cv.waitKey(0)
cv.destroyAllWindows()

cv.imshow('logo', logo)
cv.waitKey(0)
cv.destroyAllWindows()

row, width, chanell = image.shape
roi = image[row - 108: row, width - 108:width]

gray_logo = cv.cvtColor(logo, cv.COLOR_BGR2GRAY)
ret, mask = cv.threshold(gray_logo, 200, 255, cv.THRESH_BINARY_INV)
mask_inv = cv.bitwise_not(mask)


image_bg = cv.bitwise_and(roi, roi, mask=mask_inv)
cv.imshow('image_bg', image_bg)
cv.waitKey(0)
cv.destroyAllWindows()

logo_fg = cv.bitwise_and(logo, logo, mask=mask)
cv.imshow('logo_fg', logo_fg)
cv.waitKey(0)
cv.destroyAllWindows()

result = cv.add(image_bg, logo_fg)
image[row - 108: row, width - 108:width] = result
cv.imshow('image', image)
cv.waitKey(0)
cv.destroyAllWindows()