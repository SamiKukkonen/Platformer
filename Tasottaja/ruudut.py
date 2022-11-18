import pygame
vihrea = (34,139,34)
class Ruutu(pygame.sprite.Sprite):
    def __init__(self,sijainti,koko):
        super().__init__()
        self.image = pygame.Surface((koko, koko))
        self.image.fill(vihrea)
        self.rect = self.image.get_rect(topleft = sijainti)
    def update(self,x_siirto):
        self.rect.x += x_siirto