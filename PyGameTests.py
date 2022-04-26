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

    pygame.draw.rect(wn, (165, 42, 42), (0, 400, 640, 80))
    pygame.draw.rect(wn, (128, 0, 0), (0, 400, 640, 10))
    pygame.draw.rect(wn, (139, 0, 139), (200, 360, 40, 40))
    pygame.draw.circle(wn, (46, 139, 87), (280, 380), 20)

    pygame.display.update()