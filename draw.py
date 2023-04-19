import cv2 as cv
import numpy as np

blank = np.zeros((500,500, 3), dtype='uint8')

#Draw line
cv.line(blank,(0,0),(511,511),(255,0,0),5)
cv.imshow('Line', blank)

#Draw rectangle
cv.rectangle(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (0,255,0), thickness=2)
cv.imshow('Rectangle', blank)

cv.circle(blank,(447,63), 63, (0,0,255), -1)
cv.imshow('Circle', blank)

#Write text
cv.putText(blank, 'Hello', (225,225), cv.FONT_HERSHEY_DUPLEX, 1.5, (0,0,255), thickness=2)
cv.imshow('Text', blank)

cv.waitKey(0)