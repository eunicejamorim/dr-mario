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
x. angulo do jogador (1-4)
4. desenhar
"""

import pygame
import random

pygame.init()

screen = pygame.display.set_mode((600, 700))
#halfpill = pygame.image.load("smaller pill.png")
#teste  = pygame.image.load("50 pixeis.png")
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


virus_pill = [
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
    ["v","v","v","v","v","v","v","v"],
    ["v","v","v","v","v","v","v","v"],
    ["v","v","v","v","v","v","v","v"],
    ["v","v","v","v","v","v","v","v"],
]

COLORS = {1: (0, 255, 0), 2: (255, 0, 0), 3: (0, 0, 255), 4: (255, 0, 255)}

#conecções entre os blocos 
#CON_ROW = {'r': 0, 'l': 0, 'u': -1, 'd': 1, 0: 0, 'v': 0}
#CON_COL = {'r': 1, 'l': -1, 'u': 0, 'd': 0, 0: 0, 'v': 0}
CONEC = {'r': 1, 'l': -1, 'u': 2, 'd': -2, 0: 0, 'v': 0}


TILE_WIDTH = 50
GRID_WIDTH = len(matrix[0])
GRID_HEIGHT = len(matrix)

MARGIN_LEFT = 0
MARGIN_TOP = 0

FALL_TIME = 1000  # ms
DESLOC_TIME = 300 #ms 

last_fall_time = 0
last_desloc_time = 0

player_row_1 = 0
player_col_1 = 0
player_row_2 = 0
player_col_2 = 1
player_color_1 = random.randrange(1, 4+1)
player_color_2 = random.randrange(1, 4+1)
player_state_1 = "l"
player_state_2 = "r"

next_player_color_1 = random.randrange(1, 4+1)
next_player_color_2 = random.randrange(1, 4+1)

# pygame.font.get_fonts()
font = pygame.font.SysFont('arial', 18) 
clock = pygame.time.Clock()

#verificar se alguma peça está a ser deslocada
desloc = False
next_same_row = True
next_same_col = True

all_changes = []
  
while running:
    dt = clock.tick(30)
    
    # eventos
    down_pressed = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and desloc == False:
            if event.key == pygame.K_LEFT and (player_col_1>=0 and player_col_2>=0):
                if player_col_1 > 0 and player_col_2 > 0 and matrix[player_row_1][player_col_1 -1] == matrix[player_row_2][player_col_2 -1] == 0:
                    player_col_1 -= 1
                    player_col_2 -= 1
            if event.key == pygame.K_RIGHT and (player_col_1<=6 and player_col_2<=6):
                if player_col_1 < len(matrix[0]) and player_col_2 < len(matrix[0]) and matrix[player_row_1][player_col_1 +1] == matrix[player_row_2][player_col_2 +1] == 0:
                    player_col_1 += 1
                    player_col_2 += 1
            if event.key == pygame.K_DOWN:
                down_pressed = True
            #rodar 
            if event.key == pygame.K_SPACE:
                if player_row_1 == player_row_2 and player_col_1 < player_col_2 and matrix[player_row_1 + 1][player_col_1] == 0 and player_row_1 != 12 and matrix[player_row_2 + 1][player_col_2 ] == 0 :
                    player_row_2 += 1
                    player_col_2 -= 1
                    player_state_1 = "u"
                    player_state_2 = "d"
                else:
                    if player_col_1 == player_col_2 and player_row_1 < player_row_2 and player_col_1 > 0 and matrix[player_row_1][player_col_1 - 1] == 0 and matrix[player_row_2][player_col_2-1] == 0 :
                        player_row_2 -= 1
                        player_col_2 -= 1
                        player_state_1 = "r"
                        player_state_2 = "l"
                    else: # rever
                        if player_row_1 == player_row_2 and player_col_1 > player_col_2 and matrix[player_row_1 -1][player_col_1] == 0 and player_row_1 > 0 and matrix[player_row_2 - 1][player_col_2] == 0 :
                            player_row_2 -= 1
                            player_col_2 += 1
                            player_state_1 = "d"
                            player_state_2 = "u"
                        else:
                            if player_col_1 == player_col_2 and player_row_1 > player_row_2  and player_col_1 < 7 and matrix[player_row_1][player_col_1 + 1] == 0 and matrix[player_row_2][player_col_2 +1] == 0 :
                                player_row_2 += 1
                                player_col_2 += 1
                                player_state_1 = "l"
                                player_state_2 = "r"

    # movimento
    if desloc == False:
        if ((pygame.time.get_ticks() - last_fall_time) > FALL_TIME or down_pressed):
            if player_row_1 + 1 <= 13 and player_row_2 + 1 <= 13 and matrix[player_row_1+1][player_col_1] == 0 and matrix[player_row_2+1][player_col_2] == 0:
                player_row_1 += 1
                player_row_2 += 1
            else:  # colisao
                matrix[player_row_1][player_col_1] = player_color_1
                matrix[player_row_2][player_col_2] = player_color_2
                virus_pill[player_row_1][player_col_1] = player_state_1
                virus_pill[player_row_2][player_col_2] = player_state_2
                player_row_1 = 0
                player_col_1 = 0
                player_row_2 = 0
                player_col_2 = 1
                player_color_1 = next_player_color_1
                player_color_2 = next_player_color_2
                player_state_1 = "l"
                player_state_2 = "r"
                next_player_color_1 = random.randrange(1, 4+1)
                next_player_color_2 = random.randrange(1, 4+1)
            last_fall_time = pygame.time.get_ticks()
    else:
        if (pygame.time.get_ticks() - last_desloc_time) > DESLOC_TIME:
            for col in range(8):
                for row in range(14-2, 0, -1): #evita o out of range
                    if matrix[row][col] != 0 and matrix[row+1][col] == 0 and virus_pill[row][col] ==0:
                        matrix[row+1][col] = matrix[row][col]
                        matrix[row][col] = 0
                    if col < 7:
                        if matrix[row][col] != 0 and matrix[row][col+1] != 0 and matrix[row+1][col] == matrix[row+1][col+1] == 0 and virus_pill[row][col] == "l" and virus_pill[row][col+1] =="r":
                            matrix[row+1][col] = matrix[row][col]
                            matrix[row][col] = 0
                            matrix[row+1][col+1] = matrix[row][col+1]
                            matrix[row][col+1] = 0
                    if matrix[row][col] != 0 and matrix[row-1][col] != 0 and matrix[row+1][col] == 0 and virus_pill[row][col] == "d" and virus_pill[row-1][col] == "u":
                        matrix[row+1][col] = matrix[row][col]
                        matrix[row][col] = matrix[row-1][col]
                        matrix[row-1][col] = 0
                        virus_pill[row+1][col] = "d"
                        virus_pill[row][col] = "u"
                    else:
                        desloc = False 
            last_desloc_time = pygame.time.get_ticks()

    # encontrar linhas/colunas 4 iguais e atualizar as a virus_pill 
   
    for col in range(8):
        for row in range(14):
             #análise de linhas
            if col < 8-3:
                if matrix[row][col] == matrix[row][col+1] == matrix[row][col+2] == matrix[row][col+3] != 0:
                    all_changes.append((row, col))
                    all_changes.append((row, col+1))
                    all_changes.append((row, col+2))
                    all_changes.append((row, col+3))
                    for i in [1, 2, 3, 4]:
                        if next_same_row == True:
                            if 1 <= col + 3 + i <= 7:
                                if matrix[row][col +3+ i] == matrix[row][col+3+i-1]:
                                    all_changes.append((row, col+3+i))
                                    if col + i == 7:
                                        next_same_row = False
                                else:
                                    next_same_row = False
             #análise de colunas
            if row < 14-3:
                if matrix[row][col] == matrix[row+1][col] == matrix[row+2][col] == matrix[row+3][col] != 0:
                    all_changes.append((row,col))
                    all_changes.append((row +1, col))
                    all_changes.append((row +2, col))
                    all_changes.append((row +3, col))
                    for i in [1, 2, 3, 4]:
                        if next_same_col == True:
                            if 1 <= row + 3+ i <= 13:
                                if matrix[row +3+ i][col] == matrix[row+3+i-1][col]:
                                    all_changes.append((row+3+i, col))
                                    if row + i == 13:
                                        next_same_col = False
                                else:
                                    next_same_col = False
        for r, c in all_changes:
            matrix[r][c] = 0
            virus_pill[r][c] = 0
        next_same_row = True
        next_same_col = True
        all_changes = []
                
    # deslocamento se nada tiver em baixo
    #atualização de ligações
    #teste tem a da direita (quebra de ligações)
    for col in range(8-1): #(evita o out of range)
        for row in range(14):
            if virus_pill[row][col] == "l" and virus_pill[row][col+1] != "r":
                virus_pill[row][col] = 0
    #teste tem a de baixo (quebra de ligações)
    for col in range(8): 
        for row in range(14-1):#(evita o out of range)
            if virus_pill[row][col] == "u" and virus_pill[row+1][col] != "d":
                virus_pill[row][col] = 0
    #teste tem a da esquerda (quebra de ligações)
    for col in range(1, 8):
        for row in range(14):
            if virus_pill[row][col] == "r" and virus_pill[row][col-1] != "l":
                virus_pill[row][col] = 0
    #teste tem a de cima (quebra de ligações)
    for col in range(8): 
        for row in range(1, 14):#(evita o out of range)
            if virus_pill[row][col] == "d" and virus_pill[row-1][col] != "u":
                virus_pill[row][col] = 0
    #começar a mexer
    for col in range(8):
        for row in range(14-2, 0, -1): #evita o out of range
            if matrix[row][col] != 0 and matrix[row+1][col] == 0 and virus_pill[row][col] ==0: #caso de bloco single
                desloc = True
            if col < 7:
                if matrix[row][col] != 0 and matrix[row][col+1] != 0 and matrix[row+1][col] == matrix[row+1][col+1] == 0 and virus_pill[row][col] == "l" and virus_pill[row][col+1] =="r":
                    desloc = True
            if matrix[row][col] != 0 and matrix[row-1][col] != 0 and matrix[row+1][col] == 0 and virus_pill[row][col] == "d" and virus_pill[row-1][col] == "u":
                desloc = True

    ####################################################################
    # desenhar
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (255, 255, 255), (MARGIN_LEFT+2, MARGIN_TOP+2, TILE_WIDTH*len(matrix[0])-4, TILE_WIDTH*len(matrix)-4))

    #screen.blit(halfpill, (0,0))
    for col in range(8):
        for row in range(14):
            if matrix[row][col] == 0: continue
            color = COLORS[matrix[row][col]]
            x = col*TILE_WIDTH+MARGIN_LEFT
            y = row*TILE_WIDTH+MARGIN_TOP

            pygame.draw.rect(screen, color, (x+2, y+2, TILE_WIDTH-4, TILE_WIDTH-4))
            text = font.render(str(virus_pill[row][col]), True, (255, 255, 255))
            screen.blit(text, (x+2, y+2))

    #desenhar primeiro círculo
    x = player_col_1*TILE_WIDTH+MARGIN_LEFT
    y = player_row_1*TILE_WIDTH+MARGIN_TOP
    pygame.draw.circle(screen, COLORS[player_color_1], (x+TILE_WIDTH//2, y+TILE_WIDTH//2), TILE_WIDTH//2)
    #desenhar segundo círculo
    x = (player_col_2)*TILE_WIDTH+MARGIN_LEFT
    y = player_row_2 *TILE_WIDTH+MARGIN_TOP
    pygame.draw.circle(screen, COLORS[player_color_2], (x+TILE_WIDTH//2, y+TILE_WIDTH//2), TILE_WIDTH//2)
    

    # NEXT
    x = MARGIN_LEFT + len(matrix[0])*TILE_WIDTH + 10
    y = MARGIN_TOP + 10
    pygame.draw.circle(screen, COLORS[next_player_color_1], (x+TILE_WIDTH//2, y+TILE_WIDTH//2), TILE_WIDTH//2)
    #desenhar segundo círculo
    x = MARGIN_LEFT + len(matrix[0])*TILE_WIDTH + 10 + TILE_WIDTH
    pygame.draw.circle(screen, COLORS[next_player_color_2], (x+TILE_WIDTH//2, y+TILE_WIDTH//2), TILE_WIDTH//2)

    pygame.display.flip()

pygame.quit()