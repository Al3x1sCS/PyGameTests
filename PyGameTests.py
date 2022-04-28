import pygame
import Utils.Colors
from pygame import *

pygame.init()

# Mark: Constantes do jogo
# --tela--
WIDTH = 450
HEIGHT = 300
dimensions = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(dimensions)
pygame.display.set_caption('Endlesscape')
background = Utils.Colors.black
fps = 60
font = pygame.font.Font('freesansbold.ttf', 16)
timer = pygame.time.Clock()

# Mark: Variáveis do Jogo
score = 0
player_x = 50
player_y = 200
running = True
y_change = 0
x_change = 0
gravity = 1

# Mark: Loop Principal
# Enquanto o jogo estiver rodando
while running:
    timer.tick(fps)
    screen.fill(background)
    floor = pygame.draw.rect(screen, Utils.Colors.white, [0, 220, WIDTH, 5])
    player = pygame.draw.circle(screen, Utils.Colors.darkmagenta, [player_x, player_y], 20)
    # PARA cada evento no jogo testa se uma tecla está sendo pressionada ou não.
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
        # Teclas A, W, S, D
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w and y_change == 0:
                y_change = 14
            if event.key == pygame.K_d:
                x_change = 2
            if event.key == pygame.K_a:
                x_change = -2
            if event.key == pygame.K_s:
                x_change = 0
        # SE a tecla não estiver pressionada o movimento sera nulo.
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                x_change = 0
            if event.key == pygame.K_a:
                x_change = 0
            if event.key == pygame.K_s:
                x_change = 0
    # X
    # Se certifica que o jogador esta dentro da tela no eixo X
    if 0 <= player_x <= 430:
        player_x += x_change
    if player_x < 0:
        player_x = 0
    if player_x > 430:
        player_x = 430
    # Y
    # Se certifica que o jogador caia quando pula.
    if y_change > 0 or player_y < 200:
        player_y -= y_change
        y_change -= gravity
    if player_y > 200:
        player_y = 200
    if player_y == 200 and y_change < 0:
        y_change = 0

    pygame.display.flip()
    
pygame.quit()
