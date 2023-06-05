"""
Logica interna modulo Pica Pared

"""

#Librerias
import time
import random
import pygame
import RPi.GPIO as GPIO

from moduleDeteccion import *
from communication import *


def picaPared():

	# Preparar juego

	# Audio
	pygame.mixer.init()
	soundInicio = pygame.mixer.Sound('')
	sound123picapared = pygame.mixer.Sound('audios/123picapared.ogg')
	sound123ya = pygame.mixer.Sound('audios/123ya.ogg')
	soundPillado = pygame.mixer.Sound('')
	soundWin = pygame.mixer.Sound('')
	soundLose = pygame.mixer.Sound('')
	
	# Boton
	BUTTON_PIN = 15
	GPIO.setwarnings(False)
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
	
	buttonPressed = False
	def buttonCallback(channel):
		buttonPressed = True
		
	GPIO.add_event_detect(BUTTON_PIN, GPIO.RISING, callback=buttonCallback)
	
	# Ruedas
	ard_com = ArduinoCommunication()
    	time.sleep(2)
	
	comandoGiroM1 = CatchProtocol.command_to_binary(CatchProtocol.COMMAND.SET_MOTOR_1, CatchProtocol.DIRECTIONS.DIRECTIONS_FORWARD, 200)
	comandoGiroM2 = CatchProtocol.command_to_binary(CatchProtocol.COMMAND.SET_MOTOR_2, CatchProtocol.DIRECTIONS.DIRECTIONS_FORWARD, 200)
	comandoStopM1 = CatchProtocol.command_to_binary(CatchProtocol.COMMAND.SET_MOTOR_1, CatchProtocol.DIRECTIONS.STOP, 0)
	comandoStopM2 = CatchProtocol.command_to_binary(CatchProtocol.COMMAND.SET_MOTOR_2, CatchProtocol.DIRECTIONS.STOP, 0)
	
	# Deteccion de personas
	th = 25

	
	# Audio comienzo juego
	playing = soundInicio.play()
	while playing.get_busy():
		pygame.time.delay(100)

	while not buttonPressed: #(boton no pulsado)
		#Girar 180
		ard_com.send_message(comandoGiroM1)
		ard_com.send_message(comandoGiroM2)
		time.sleep(5)
		ard_com.send_message(comandoStopM1)
		ard_com.send_message(comandoStopM2)

		# Audio "123 picapared"
		playing = sound123picapared.play()
		while playing.get_busy():
			pygame.time.delay(100)

		# Esperar entre 0 a 5 segundos
		t = random.randrange(0, 5, 1)
		print("Esperando " + str(t) + " segundos")
		time.sleep(t)

		#Girar 180
		ard_com.send_message(comandoGiroM1)
		ard_com.send_message(comandoGiroM2)
		time.sleep(5)
		ard_com.send_message(comandoStopM1)
		ard_com.send_message(comandoStopM2)

		# Audio "123 ya!"
		playing = sound123ya.play()
		while playing.get_busy():
			pygame.time.delay(100)

		# Deteccion Movimiento
		mov = deteccionMov(th)
		
		if mov == True:
			# Audio "Te he pillado"
			playing = soundPillado.play()
			while playing.get_busy():
				pygame.time.delay(100)
			break

	
	if mov == True:
		playing = soundWin.play()
		while playing.get_busy():
			pygame.time.delay(100)
	else:
		playing = soundLose.play()
		while playing.get_busy():
			pygame.time.delay(100)
	
	GPIO.cleanup()

	return 0


if __name__ == '__main__':
	
    # Juego Pica Pared
    ret = picaPared()
    print(ret)
