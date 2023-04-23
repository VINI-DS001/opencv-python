import cv2 as cv
import numpy as np

#Converts bgr values to hsv, use trackbar.py as auxiliary tool
blue = np.uint8([[[255,0,0]]])
hsv_blue = cv.cvtColor(blue,cv.COLOR_BGR2HSV)
print( hsv_blue )