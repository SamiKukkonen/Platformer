import pygame, sys
from asetukset import *
from taso1 import Taso

pygame.init()
screen = pygame.display.set_mode((LEVEYS, KORKEUS))
kello = pygame.time.Clock()
taso = Taso(taso_pinta, screen)
#Peli loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill("white")
    taso.run()
    pygame.display.update()
    kello.tick(60)