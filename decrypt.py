import numpy as np
import cv2

#In decrypt.png, there are two types of pixels of different intensities

img = cv2.imread('decrypt.png',0)

#You need to apply thresholding to decrypt this image to get the hidden message of supreme importance!
#Hint you are given key "12"
img=cv2.threshold(img,12,255,cv2.THRESH_BINARY)
cv2.imshow('threshold', img)
cv2.waitKey(0)
cv2.destroyAllWindows()