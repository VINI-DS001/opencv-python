import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('photos/forest.jpg', 0)
rows,cols = img.shape

#Main interpolation methods: cv.INTER_AREA, cv.INTER_CUBIC and cv.INTER_LINEAR
res = cv.resize(img, None, fx=0.5, fy=0.5, interpolation=cv.INTER_CUBIC)

#Translates object's location
M = np.float32([[1,0,100],[0,1,50]])
dst = cv.warpAffine(img,M,(cols,rows))

#Rotates an image, cols-1 and rows-1 are coordinate limits
M = cv.getRotationMatrix2D(((cols-1)/2.0,(rows-1)/2.0),90,1)
rot = cv.warpAffine(img,M,(cols,rows))

#Perspective change, create an image with the output as a matrix.
pts1 = np.float32([[56,65],[368,52],[28,387],[389,390]])
pts2 = np.float32([[0,0],[300,0],[0,300],[300,300]])
M = cv.getPerspectiveTransform(pts1,pts2)
dst = cv.warpPerspective(img,M,(300,300))
plt.subplot(121),plt.imshow(img),plt.title('Input')
plt.subplot(122),plt.imshow(dst),plt.title('Output')
plt.show()

cv.imshow('Resized Image', res)
cv.imshow('Translated',dst)
cv.imshow('Rotated', rot)


cv.waitKey(0)