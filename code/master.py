"""
Module para Seleccion de Juegos

"""
import time
from modulePicaPared import *


if __name__ == '__main__':
    
    # Preparacion seleccion juegos
    time.sleep(20)
    # Audio
    pygame.mixer.init()
	soundInicio = pygame.mixer.Sound('/home/pi/Desktop/MsCatchME/code/audios/HolaSoyMsCatchMe.wav')
	soundPicaPared = pygame.mixer.Sound('/home/pi/Desktop/MsCatchME/code/audios/Pulsa1PicaPared.wav')
	# Boton
	BUTTON_PIN = 15
	GPIO.setwarnings(False)
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
	
	buttonPressed = False
	def buttonCallback(channel):
		buttonPressed = True
		
	GPIO.add_event_detect(BUTTON_PIN, GPIO.RISING, callback=buttonCallback)
	# Audio seleccion juegos
    playing = soundInicio.play()
    while playing.get_busy():
        pygame.time.delay(100)
    playing = soundPicaPared.play()
    while playing.get_busy():
        pygame.time.delay(100)
        
    while True:

        if buttonPressed: # Comprovar boton pulsado 1 vez
            picaPared()
        else:
            if(False): # Comprovar boton pulsado 2 veces
                print()
            else:
                if(False): # Comprovar boton pulsado 3 veces
                    print()