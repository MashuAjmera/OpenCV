import cv2
import numpy as np
img = cv2.imread('board.jpg',0)
rows,cols = img.shape
# cv2.getRotationMatrix2D(rotation_center_x, rotation_center_y, angle of rotation, scale)
rotation_matrix = cv2.getRotationMatrix2D((cols/2,rows/2),90,1)
# cv2.warpAffine(image, translation_matrix, (width,height))
rotated_image = cv2.warpAffine(img,rotation_matrix,(cols,rows))
cv2.imshow('output', rotated_image)
cv2.waitKey(0)
cv2.destroyAllWindows()