"""
Logica interna modulo Pica Pared

"""

#Librerias
import time
import random

from moduleDeteccion import *

def picaPared():
	th = 25
	
	# Audio comienzo juego


	# Bucle principal
	while True: #(boton no pulsado)
		# Audio "123 picapared"
		t = random.randrange(0, 5, 1)
		time.sleep(t)
		# Audio "123 ya!"
		mov = deteccionMov(th)
		if mov == True:
			# Audio "Te he visto! vuelve al inicio"
			
	# Audio "Has ganado!"
