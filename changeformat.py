import numpy as np
import cv2
####### FOR IMAGE READING ######
img=cv2.imread('board.jpg',1)
####### FOR CHANGING IMAGE FORMAT ######
cv2.imwrite('my_image.png',img)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()