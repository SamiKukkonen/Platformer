from sys import _xoptions
import pygame
from ruudut import Ruutu
from asetukset import ruutu_koko, LEVEYS
from pelaaja import Pelaaja
class Taso:
    def __init__(self, taso_data, surface):
        self.display_surface = surface
        self.taso_asetukset(taso_data)
        self.taso_siirto = 0
    def siirto_x(self):
        pelaaja = self.pelaaja.sprite
        pelaaja_x = pelaaja.rect.centerx
        suunta_x = pelaaja.suunta.x

        if pelaaja_x < LEVEYS / 3 and suunta_x < 0:
            self.taso_siirto = 8
            pelaaja.nopeus = 0
        elif pelaaja_x > LEVEYS - (LEVEYS / 3) and suunta_x > 0:
            self.taso_siirto = -8
            pelaaja.nopeus = 0
        else:
            self.taso_siirto = 0
            pelaaja.nopeus = 8
    def taso_asetukset(self, pohja):
        self.ruudut = pygame.sprite.Group()
        self.pelaaja = pygame.sprite.GroupSingle()
        for rivi_index,rivi in enumerate(pohja):
            for jono_index, cell in enumerate(rivi):
                x = rivi_index * ruutu_koko
                y = jono_index * ruutu_koko
                if cell == "X":
                    ruutu = Ruutu((y,x), ruutu_koko)
                    self.ruudut.add(ruutu)
                if cell == "O":
                    pelaaja_hahmo = Pelaaja((y, x))
                    self.pelaaja.add(pelaaja_hahmo)
    def sivuttainen_liike(self):
        pelaaja = self.pelaaja.sprite
        pelaaja.rect.x += pelaaja.suunta.x * pelaaja.nopeus
        for sprite in self.ruudut.sprites():
            if sprite.rect.colliderect(pelaaja.rect):
                if pelaaja.suunta.x < 0:
                    pelaaja.rect.left = sprite.rect.right
                elif pelaaja.suunta.x > 0:
                    pelaaja.rect.right = sprite.rect.left
    def pysty_liike(self):
        pelaaja = self.pelaaja.sprite
        pelaaja.painovoima()
        for sprite in self.ruudut.sprites():
            if sprite.rect.colliderect(pelaaja.rect):
                if pelaaja.suunta.y > 0:
                    pelaaja.rect.bottom = sprite.rect.top
                    pelaaja.suunta.y = 0
                elif pelaaja.suunta.y < 0:
                    pelaaja.rect.top = sprite.rect.bottom
                    pelaaja.suunta.y = 0
    def run(self):
        #Ruudut
        self.ruudut.update(self.taso_siirto)
        self.ruudut.draw(self.display_surface)
        #Pelaaja
        self.pelaaja.update()
        self.sivuttainen_liike()
        self.pysty_liike()
        self.pelaaja.draw(self.display_surface)
        self.siirto_x()