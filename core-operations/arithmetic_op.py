import cv2 as cv

img = cv.imread('photos/forest.jpg')

img2 = cv.imread('photos/wall-e.jpg')

#Images size must match, otherwise it won't work
res = cv.addWeighted(img,0.7,img2,0.3,0)
cv.imshow('Result', res)

cv.waitKey(0)

cv.destroyAllWindows()