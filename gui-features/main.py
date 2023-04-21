import cv2 as cv
import numpy as np
# Showing image
img = cv.imread('photos/city.jpg')

cv.imshow('City', img)

cv.waitKey(0)

#Showing video
capture = cv.VideoCapture('videos/sea.mp4')

while True:
    isTrue, frame = capture.read()

    cv.imshow('Video', frame)
    # Press 'e' in keyboard to interrupt video
    if cv.waitKey(20) & 0xFF==ord('e'):
        break

capture.release()
cv.destroyAllWindows()