"""
Module Seleccion Juegos

"""

import cv2 

cam = cv2.VideoCapture(0)

while True:
	ret, img = cam.read()
	cv2.imshow('Imagetest', img)
	k = cv2.waitKey(1)
	if k != -1:
		break
		
cv2.imwrite('/home/pi/testimage.jpg', img)
cam.release()
cv2.destroyAllWindows()
