import pygame
from pygame import *
from sys import exit

pygame.init()

# Mark: Tema

brown = (139, 69, 19)
black = (0, 0, 0)
blue = (0, 0, 255)
darkmagenta = (139, 0, 139)
cabon = (47, 79, 79)
green = (0, 100, 00)
indigo = (75, 0, 130)
red = (128, 0, 0)
white = (255, 255, 255)

# Mark: Tela

dimensions = (640, 480)
janela = pygame.display.set_mode(dimensions)
pygame.display.set_caption('PyGameTests')

# Mark: Loop Principal

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    pygame.draw.rect(janela, brown, (0, 400, 640, 80))
    pygame.draw.rect(janela, green, (0, 400, 640, 20))
    pygame.draw.rect(janela, red, (280, 370, 40, 40))
    pygame.draw.circle(janela, darkmagenta, (200, 390), 20)

    pygame.display.update()
