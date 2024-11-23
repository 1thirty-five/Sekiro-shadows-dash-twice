import pygame
import sys

pygame.init() # Initializes pygame

pygame.display.set_caption('Ninja Platformer')
screen = pygame.display.set_mode((640,480)) #provides display screen

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.QUIT()
            sys.exit()
    
    pygame.display.update()
    clock.tick(60)
    



