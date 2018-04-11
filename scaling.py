import cv2
import numpy as np
######### FOR SCALING ######
img = cv2.imread('board.jpg',0)
#cv2.resize(image, dsize(output image size), x scale, y scale, interpolation)
res = cv2.resize(img,None,fx=1.5, fy=1.5, interpolation = cv2.INTER_CUBIC)
cv2.imshow('scaled-image',res)
cv2.waitKey(0)
cv2.destroyAllWindows()
#Matplotlib is a plotting library for Python which gives you wide variety of plotting methods
#OpenCV stores image in form of BGR whereas the other one stores in RGB
#RED and BLUE planes will be interchanged