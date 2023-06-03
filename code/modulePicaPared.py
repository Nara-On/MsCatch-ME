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

pygame.mixer.init()
buttonPressed = False

def picaPared():

	# Preparar juego

	# Audio
	#soundInicio = pygame.mixer.Sound("/home/pi/Desktop/MsCatchME/code/audios/123ya.ogg")
	soundInicio = pygame.mixer.Sound('/home/pi/Desktop/MsCatchME/code/audios/PicaPared.wav')
	sound123picapared = pygame.mixer.Sound('/home/pi/Desktop/MsCatchME/code/audios/123picapared.ogg')
	sound123ya = pygame.mixer.Sound('/home/pi/Desktop/MsCatchME/code/audios/123ya.ogg')
	soundPillado = pygame.mixer.Sound('/home/pi/Desktop/MsCatchME/code/audios/PilladoHasPerdido.wav')
	soundWin = pygame.mixer.Sound('/home/pi/Desktop/MsCatchME/code/audios/MeHasPillado.wav')
	#soundLose = pygame.mixer.Sound('audios/PilladoHasPerdido.ogg')
	
	# Boton
	BUTTON_PIN = 15
	GPIO.setwarnings(False)
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
	
	global buttonPressed
	buttonPressed = False
	def buttonCallback(channel):
		global buttonPressed
		print("Button is pressed")
		buttonPressed = True
		
	GPIO.add_event_detect(BUTTON_PIN, GPIO.RISING, callback=buttonCallback)
	
	# Ruedas
	ard_com = ArduinoCommunication()
	time.sleep(2)
	
	comandoGiroM1 = CatchProtocol.command_to_binary(CatchProtocol.COMMAND.SET_MOTOR_1, CatchProtocol.DIRECTIONS.BACKWARD, 255)
	comandoGiroM2 = CatchProtocol.command_to_binary(CatchProtocol.COMMAND.SET_MOTOR_2, CatchProtocol.DIRECTIONS.FORWARD, 255)
	comandoStopM1 = CatchProtocol.command_to_binary(CatchProtocol.COMMAND.SET_MOTOR_1, CatchProtocol.DIRECTIONS.STOP, 0)
	comandoStopM2 = CatchProtocol.command_to_binary(CatchProtocol.COMMAND.SET_MOTOR_2, CatchProtocol.DIRECTIONS.STOP, 0)
	
	# Deteccion de personas
	th = 5

	
	# Audio comienzo juego
	playing = soundInicio.play()
	while playing.get_busy():
		pygame.time.delay(100)

	while not buttonPressed: #(boton no pulsado)
		#Girar 180
		ard_com.send_message(comandoGiroM1)
		ard_com.send_message(comandoGiroM2)
		time.sleep(2)
		if buttonPressed:
			break
		ard_com.send_message(comandoStopM1)
		ard_com.send_message(comandoStopM2)

		# Audio "123 picapared"
		playing = sound123picapared.play()
		while playing.get_busy():
			pygame.time.delay(100)
		if buttonPressed:
			break

		# Esperar entre 0 a 2 segundos
		#t = random.randrange(0, 2, 1)
		#print("Esperando " + str(t) + " segundos")
		time.sleep(1)
		if buttonPressed:
			break

		#Girar 180
		ard_com.send_message(comandoGiroM1)
		ard_com.send_message(comandoGiroM2)
		time.sleep(2)
		if buttonPressed:
			break
		ard_com.send_message(comandoStopM1)
		ard_com.send_message(comandoStopM2)

		# Audio "123 ya!"
		playing = sound123ya.play()
		while playing.get_busy():
			pygame.time.delay(100)
		if buttonPressed:
			break

		# Deteccion Movimiento
		mov = deteccionMov(th)
		
		if mov == True:
			# Audio "Te he pillado"
			playing = soundPillado.play()
			while playing.get_busy():
				pygame.time.delay(100)
			break

	
	if buttonPressed:
		playing = soundWin.play()
		while playing.get_busy():
			pygame.time.delay(100)
	"""
	else:
		playing = soundLose.play()
		while playing.get_busy():
			pygame.time.delay(100)
	"""
	GPIO.cleanup()

	return 0


if __name__ == '__main__':
	time.sleep(0.5)
	
	# Juego Pica Pared
	ret = picaPared()
	print(ret)
