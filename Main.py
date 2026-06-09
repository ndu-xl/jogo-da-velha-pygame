import pygame
import Menu
import PvP
import PvE
pygame.init()

#adiciona a musica tema
pygame.mixer.music.set_volume(0.1)
trilha_sonora = pygame.mixer.music.load('Trilha Sonora.mp3')
pygame.mixer.music.play(-1)

state = "menu" #começa no menu

while True: #repete até o modo ser trocado

    if state == "menu":
        state = Menu.MenuPage()

    elif state == "pvp":
        state = PvP.PvPPage()
    
    elif state == "pve":
        state = PvE.PvEPage()