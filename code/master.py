"""
Module para Seleccion de Juegos

"""

from modulePicaPared import *


if __name__ == '__main__':
    
    # Preparacion seleccion juegos
    
    # Audio
    pygame.mixer.init()
	soundInicio = pygame.mixer.Sound('')
    
    # Boton
	BUTTON_PIN = 15
	GPIO.setwarnings(False)
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
	
	buttonPressed = False
	def buttonCallback(channel):
		buttonPressed = True
		
	GPIO.add_event_detect(BUTTON_PIN, GPIO.RISING, callback=buttonCallback)
    
    
    while True:
        # Audio seleccion juegos
        playing = soundInicio.play()
        while playing.get_busy():
            pygame.time.delay(100)
        
        if buttonPressed: # Comprovar boton pulsado 1 vez
            picaPared()
        else:
            if(False): # Comprovar boton pulsado 2 veces
                print()
            else:
                if(False): # Comprovar boton pulsado 3 veces
                    print()
