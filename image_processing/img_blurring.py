import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('photos/forest.jpg')

blur = cv.blur(img,(5,5))

#Gaussian Blur
blurGaussian = cv.GaussianBlur(img,(5,5),0)

#Median Blurring
median  = cv.medianBlur(img, 5)

#Bilateral Blurring
blurBilateral = cv.bilateralFilter(img,9,75,75)

plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(blur),plt.title('Blurred')
plt.xticks([]), plt.yticks([])
plt.show()