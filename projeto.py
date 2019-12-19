# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 12:10:22 2019

@author: eunic
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 11:40:02 2019

@author: eunic
"""

"""
X. nao deixar sair das paredes
2. ter duas variaveis para a cor do jogador (lista com dois elementos)
3. angulo do jogador (1-4)
4. desenhar
"""

import pygame
import random

pygame.init()

screen = pygame.display.set_mode((600, 700))
#halfpill = pygame.image.load("smaller pill.png")
teste  = pygame.image.load("50 pixeis.png")
running = True

matrix = [
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [3,3,1,4,1,2,1,2],
    [3,2,4,4,4,2,3,2],
    [3,1,3,2,2,1,3,4],
    [1,1,1,2,4,4,3,2],
]

'''
is_pill = [
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
]
'''

COLORS = {1: (0, 255, 0), 2: (255, 0, 0), 3: (0, 0, 255), 4: (255, 0, 255)}
TILE_WIDTH = 50
GRID_WIDTH = len(matrix[0])
GRID_HEIGHT = len(matrix)

MARGIN_LEFT = 0
MARGIN_TOP = 0

FALL_TIME = 1000  # ms

last_fall_time = 0
player_row = 0
player_col = 0
player_color = random.randrange(1, 4+1)

clock = pygame.time.Clock()
  
while running:
    dt = clock.tick(30)
    
    # eventos
    down_pressed = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and player_col>=0:
                if player_col > 0:
                    player_col -= 1
            if event.key == pygame.K_RIGHT and player_col<=6 :
                if player_col < len(matrix[0]):
                    player_col += 1
            if event.key == pygame.K_DOWN:
                down_pressed = True

    # movimento
    if (pygame.time.get_ticks() - last_fall_time) > FALL_TIME or down_pressed:
        if matrix[player_row+1][player_col] == 0:
            player_row += 1
        else:  # colisao
            matrix[player_row][player_col] = player_color
            player_row = 0
            player_col = 0
            player_color = random.randrange(1, 4+1)
        last_fall_time = pygame.time.get_ticks()

    # encontrar linhas/colunas 4 iguais
    for col in range(8-3):
        for row in range(14):
            if matrix[row][col] == matrix[row][col+1] == matrix[row][col+2] == matrix[row][col+3] != 0:
                matrix[row][col] = 0
                matrix[row][col+1] = 0
                matrix[row][col+2] = 0
                matrix[row][col+3] = 0
    for col in range(8):
        for row in range(14-3):
            if matrix[row][col] == matrix[row+1][col] == matrix[row+2][col] == matrix[row+3][col] != 0:
                matrix[row][col] = 0 
                matrix[row+1][col] = 0
                matrix[row+2][col] = 0
                matrix[row+3][col] = 0

    ####################################################################
    # desenhar
    screen.fill((0, 0, 0))

    #screen.blit(halfpill, (0,0))
    for col in range(8):
        for row in range(14):
            if matrix[row][col] == 0: continue
            color = COLORS[matrix[row][col]]
            x = col*TILE_WIDTH+MARGIN_LEFT
            y = row*TILE_WIDTH+MARGIN_TOP
            pygame.draw.rect(screen, color, (x+2, y+2, TILE_WIDTH-4, TILE_WIDTH-4))
            #screen.blit(teste, (50, 50))  # desenhar imagem
    x = player_col*TILE_WIDTH+MARGIN_LEFT
    y = player_row*TILE_WIDTH+MARGIN_TOP
    pygame.draw.circle(screen, COLORS[player_color], (x+TILE_WIDTH//2, y+TILE_WIDTH//2), TILE_WIDTH//2)

    pygame.display.flip()

pygame.quit()
