import pygame
from pygame.locals import *
from sys import exit

pygame.init()

largura = 640
altura = 480

wn = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('PyGameTests')

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    pygame.display.update()
