import cv2 as cv
import numpy as np

img = cv.imread('photos/wall-e.jpg', 0)

kernel = np.ones((5,5),np.uint8)

erosion = cv.erode(img,kernel,iterations = 1)

dilation = cv.dilate(img,kernel,iterations = 1)

opening = cv.morphologyEx(img, cv.MORPH_OPEN, kernel)

closing = cv.morphologyEx(img, cv.MORPH_CLOSE, kernel)

cv.imshow('Result', img)
cv.waitKey(0)

