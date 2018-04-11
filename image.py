import numpy as np
import cv2
####### FOR IMAGE READING ######
img=cv2.imread('board.jpg',1)
####### FOR SHOWING FIGURES ABOUT MENTIONED POINTS ######
#cv2.line(file_variable,starting coordinate,end coordinate,BGR,width)
cv2.line(img,(0,0),(200,300),(255,255,255),50)
#cv2.rectangle(file_variable,top left,bottom right,BGR,width)
cv2.rectangle(img,(150,250),(100,50),(0,0,255),15)
#cv2.circle(file_name,centre,radius,BGR,width)
cv2.circle(img,(47,63),63,(0,55,0),-1)
cv2.ellipse(img,(256,256),(100,50),0,0,180,255,-1)
pts=np.array([[100,50],[200,300],[700,200],[500,100]],np.int32)
pts=pts.reshape((-1,1,2))
cv2.polylines(img,[pts],True,(0,255,255),3)
####### FOR WRITING SOMETHING ######
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'OpenCV',(10,300), font, 3,(0,255,255),1,cv2.LINE_AA)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()