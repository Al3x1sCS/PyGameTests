import pygame
from pygame import *

pygame.init()

# Mark: Constantes do jogo

# --tema--
brown = (139, 69, 19)
black = (0, 0, 0)
blue = (0, 0, 255)
darkmagenta = (139, 0, 139)
carbon = (47, 79, 79)
green = (0, 100, 00)
indigo = (75, 0, 130)
red = (128, 0, 0)
white = (255, 255, 255)

# --tela--
WIDTH = 450
HEIGHT = 300
dimensions = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(dimensions)
pygame.display.set_caption('Endlesscape')
background = carbon
fps = 60
font = pygame.font.Font('freesansbold.ttf', 16)
timer = pygame.time.Clock()

# Mark: Variáveis do Jogo
score = 0
player_x = 50
player_y = 200
running = True
y_change = 0
gravity = 1

# Mark: Loop Principal

while running:
    timer.tick(fps)
    screen.fill(background)
    floor = pygame.draw.rect(screen, white, [0, 220, WIDTH, 5])
    player = pygame.draw.circle(screen, darkmagenta, [player_x, player_y], 20)

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and y_change == 0:
                y_change = 18

    if y_change > 0 or player_y < 200:
        player_y -= y_change
        y_change -= gravity
    if player_y > 200:
        player_y = 200
    if player_y == 200 and y_change < 0:
        y_change = 0

    pygame.display.flip()
pygame.quit()
