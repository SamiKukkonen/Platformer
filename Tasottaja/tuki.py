from os import walk
import pygame
def import_folder(path):
    pinta_lista = []
    for _,__,kuva_tiedostot in walk(path):
        for kuva in kuva_tiedostot:
            koko_polku = path + "/" + kuva
            kuva_pinta = pygame.image.load(koko_polku).convert_alpha()
            pinta_lista.append(kuva_pinta)
    return pinta_lista