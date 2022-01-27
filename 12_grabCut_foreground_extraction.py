import cv2 as cv
import numpy as np

image = cv.imread('test.jpeg')
cv.imshow('image', image)
cv.waitKey(0)
cv.destroyAllWindows()

mask = np.zeros(image.shape[:2],np.uint8)

bgdModel = np.zeros((1,65),np.float64)
fgdModel = np.zeros((1,65),np.float64)

rect = (250, 80, 300, 500)

cv.grabCut(image, mask, rect, bgdModel, fgdModel, 5, cv.GC_INIT_WITH_RECT)

mask2 = np.where((mask==2) | (mask==0), 0, 1).astype('uint8')
deleted_bg_image = image * mask2[:,:,np.newaxis]
cv.imshow('img', deleted_bg_image)
cv.waitKey(0)
cv.destroyAllWindows()