import numpy as np
import cv2

#Read image boroque.jpg
img = cv2.imread('baroque.jpg',1)


#Using our face detector, we have detected a face in this image
#A rectangle covering this face has top-left coordinates (x,y) and width and height w and h.

#x,y,w,h = (116,42,62,62)
cv2.rectangle(img,(116,42),(178,104),(255,0,0),2)
# Using OpenCV draw a rectangle around this face using given data and show this new image.


cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()