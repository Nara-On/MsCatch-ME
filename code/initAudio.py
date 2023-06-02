import pygame

pygame.mixer.init()

sound = pygame.mixer.Sound('/home/pi/Desktop/code/audio/123ya.ogg')
playing = sound.play()

while playing.get_busy():
    pygame.time.delay(100)
