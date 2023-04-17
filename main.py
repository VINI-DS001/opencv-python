import cv2 as cv
import numpy as np

img = cv.imread('photos/city.jpg')

cv.imshow('Beach', img)

cv.waitKey(0)