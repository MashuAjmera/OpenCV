import numpy as np
import cv2

#Read image board.jpg
img = cv2.imread('board.jpg')


#Using our detector, we have detected the corner points given in the list
#[top-left , top-right , bottom-left , bottom-right].

#corners = [ (38,75),
#            (306,28),
#            (90,288),
#            (417,160) ]

#Using Affine Transformation, generate a top view of this board
rows,cols,ch = img.shape
pts1 = np.float32([[38,75],[306,28],[90,288],[417,160]])
pts2 = np.float32([[0,0],[500,0],[0,300],[500,300]])
M = cv2.getPerspectiveTransform(pts1,pts2)
dst = cv2.warpPerspective(img,M,(500,300))
cv2.imshow('input',img)
cv2.imshow('output',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()