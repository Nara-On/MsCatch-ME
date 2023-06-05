"""
Module Deteccion de personas o movimiento

"""

# Llibreries
import cv2 
import time
import random


def deteccionMov(thMax):

	cam = cv2.VideoCapture(0)
	imgList = []
	
	n = random.randrange(100, 200, 1)
	i = 0
	
	_, start = cam.read()
	start = cv2.cvtColor(start, cv2.COLOR_BGR2GRAY)
	start = cv2.GaussianBlur(start, (21,21), 0)
	
	mov = False
	
	
	while i < n:
		_, frame = cam.read()
		frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		frame = cv2.GaussianBlur(frame, (21,21), 0)
		
		diff = cv2.absdiff(frame, start)
		th = cv2.threshold(diff, 25, 255, cv2.THRESH_BINARY)[1]
		
		start = frame
		
		if th.sum() > thMax:
			mov = True
			break
			
		cv2.imshow('Imagetest', frame)
	
		i = i+1
		
	cam.release()
	
	print(str(n) + " total frames")
	print(str(i) + " frames read")
	return mov


def deteccionPers():	
	return 1



if __name__ == '__main__':
	bDetect = deteccionMov(200)
	print(bDetect)
