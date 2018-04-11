import cv2
import numpy as np
img = cv2.imread('board.jpg',0)
rows,cols = img.shape 
#Numpy array of data type np.float32
M = np.float32([[1,0,-100],[0,1,50]])
# cv2.warpAffine(image, translation_matrix, (width,height))
dst = cv2.warpAffine(img,M,(cols,rows))
cv2.imshow('img',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
#A numpy array is a grid of values ,of all same type.
#Shape of image is accessed by img.shape. It returns a tuple(list) of number of rows, columns and channels (if image is color):
#If image is grayscale, tuple returned contains only number of rows and columns. So it is a good method to check if loaded image is grayscale or color image.
#warpAffine method uses translation matrix of 2X3
