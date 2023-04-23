import cv2 as cv

#Show color sales to use in cv.COLOR conversion
flags = [i for i in dir(cv) if i.startswith('COLOR_')]
print( flags )

img = cv.imread('photos/forest.jpg')
cv.imshow('Forest', img)

#BGR to Grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

cv.imshow('Gray Forest', gray)

#BGR to HSV
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

cv.waitKey(0)