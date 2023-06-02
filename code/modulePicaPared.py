"""
Logica interna modulo Pica Pared

"""

#Librerias
import time
import random
import pygame

from moduleDeteccion import *
from communication import *


def picaPared():
	
    # Preparar juego
    
	pygame.mixer.init()
	sound123ya = pygame.mixer.Sound('/home/pi/Desktop/code/audio/123ya.ogg')
	sound123picapared = pygame.mixer.Sound('/home/pi/Desktop/code/audio/123picapared.ogg')
	
	th = 25
	
	
	# Audio comienzo juego


	while True: #(boton no pulsado)
		#Girar 180
		# ...
		
		# Audio "123 picapared"
		playing = sound123picapared.play()
		while playing.get_busy():
			pygame.time.delay(100)
    
		# Esperar entre 0 a 5 segundos
		t = random.randrange(0, 5, 1)
		print("Esperando " + str(t) + " segundos")
		time.sleep(t)
		
		#Girar 180
		# ...
		
		# Audio "123 ya!"
		playing = sound123ya.play()
		while playing.get_busy():
			pygame.time.delay(100)
		
		# Deteccion Movimiento
		mov = deteccionMov(th)
		if mov == True:
			# Audio "Te he visto! vuelve al inicio"
			print("Se a detectado mov!")
			
	# Audio "Has ganado!"
	print("Boton pulsado!")
	
	return 1



if __name__ == '__main__':
    
    # Connection Arduino
    ard_com = ArduinoCommunication()
    time.sleep(2)

    res = CatchProtocol.command_to_binary(CatchProtocol.COMMAND.SET_MOTOR_1, CatchProtocol.DIRECTIONS.STOP, 0)
    print(list(res))

    ard_com.send_message(res)
    ret_mess = ard_com.read_message()
    print(ret_mess)
    
    # Juego Pica Pared
    ret = picaPared()
    print(ret)
