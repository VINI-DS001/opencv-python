import cv2 as cv
import numpy as np
 
if __name__ == '__main__' :
 
    # Read the image
    im = cv.imread('photos/city.jpg')
 
    # Select ROI with mouse
    r = cv.selectROI(im)
 
    # Crop image
    imCrop = im[int(r[1]):int(r[1]+r[3]), int(r[0]):int(r[0]+r[2])]
 
    # Display cropped image
    cv.imshow("Image", imCrop)
    cv.waitKey(0)