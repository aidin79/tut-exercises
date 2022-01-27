import cv2 as cv
import numpy as np

class Helpers:
    def color_filter(self, image, lower, upper):
        hsv = cv.cvtColor(image, cv.COLOR_BGR2HSV)

        lower_range = np.array(lower)
        upper_range = np.array(upper)

        mask = cv.inRange(hsv, lower_range, upper_range)
        res = cv.bitwise_and(image, image, mask=mask)
        
        return res