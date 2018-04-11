import numpy as np
import cv2
img=cv2.imread('board.jpg',1)
####### FOR CROPPING ######
board=img[37:111,107:194]
img[0:74,0:87]=board
cv2.imshow('crop',board)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()