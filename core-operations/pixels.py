import cv2 as cv
import numpy as np

img = cv.imread('photos/forest.jpg')

print(img.shape)

print(img.size)

print(img.dtype)

cv.imshow('Forest', img)

cv.waitKey(0)