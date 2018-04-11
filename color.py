import numpy as np
import cv2
img=cv2.imread('board.jpg',1)
B,G,R=img[0,0]
#print(B,G,R)
img_hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
#cv2.imshow('image',img_hsv)
#cv2.imshow('hue Channel', img_hsv[:,:,0])
#cv2.imshow('saturation', img_hsv[:,:,1])
#cv2.imshow('value channel', img_hsv[:,:,2])
B,G,R=cv2.split(img)
#cv2.imshow('Green',G)
m_img=
cv2.imshow('hue Channel', m_img)
cv2.waitKey(0)
cv2.destroyAllWindows()