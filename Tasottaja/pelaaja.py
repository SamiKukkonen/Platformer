import pygame
from pygame.constants import K_RIGHT, K_SPACE, KEYDOWN
from tuki import import_folder
class Pelaaja(pygame.sprite.Sprite):
    def __init__(self, sijainti):
        super().__init__()
        self.tuo_pelaaja()
        self.frame_index = 0
        self.animaatio_nopeus = 0.15
        self.image = self.animaatiot["idle"][self.frame_index]
        self.rect = self.image.get_rect(topleft = sijainti)
        #pelaaja liike
        self.suunta = pygame.math.Vector2(0,0)
        self.nopeus = 6
        self.gravity = 0.8
        self.hyppy_nopeus = -16
    def tuo_pelaaja(self):
        pelaaja_polku = ("kuvat/idle1/")
        self.animaatiot = {"idle":[], "juoksu":[],"hyppy":[],"putoaminen":[]}
        for animaatio in self.animaatiot.keys():
            koko_polku = pelaaja_polku + animaatio
            self.animaatiot[animaatio] = import_folder(koko_polku)
    def komennot(self):
        komento = pygame.key.get_pressed()
        if komento[pygame.K_RIGHT]:
            self.suunta.x = 1
        elif komento[pygame.K_LEFT]:
            self.suunta.x = -1
        else:
            self.suunta.x = 0
        if komento[pygame.K_SPACE]:
            self.hyppy()
    def painovoima(self):
        self.suunta.y += self.gravity
        self.rect.y += self.suunta.y
    def hyppy(self):
        self.suunta.y = self.hyppy_nopeus
    def update(self):
        self.komennot()
