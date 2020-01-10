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

import pygame
import random
import os

pygame.init()
####screen
screen = pygame.display.set_mode((800, 790))
####está a correr
running = True
###### imagens
#todos os desenhos matriz
#1 verde/2 vermelho/3 azul/4 amarelo
UP_1 = pygame.image.load("verde_u.png")
UP_2 = pygame.image.load("verm_u.png")
UP_3 =pygame.image.load("azul_u.png")
UP_4 =pygame.image.load("ama_up.png")

DOWN_1 =pygame.image.load("verde_d.png")
DOWN_2 =pygame.image.load("verm_d.png")
DOWN_3 =pygame.image.load("azul_d.png")
DOWN_4 =pygame.image.load("ama_d.png")

RIGHT_1 =pygame.image.load("verde_r.png")
RIGHT_2 =pygame.image.load("verm_r.png")
RIGHT_3 =pygame.image.load("azul_r.png")
RIGHT_4 =pygame.image.load("ama_r.png")

LEFT_1 =pygame.image.load("verde_l.png")
LEFT_2 =pygame.image.load("verm_l.png")
LEFT_3 =pygame.image.load("azul_l.png")
LEFT_4 =pygame.image.load("ama_l.png")

SING_1 =pygame.image.load("verde_s.png")
SING_2 = pygame.image.load("verm_s.png")
SING_3 =pygame.image.load("azul_s.png")
SING_4 =pygame.image.load("ama_single.png")

VIRUS_1 =pygame.image.load("virus_verd_1.png")
VIRUS_2 =pygame.image.load("virus_verm_1.png")
VIRUS_3 =pygame.image.load("virus_azul_1.png")
VIRUS_4 =pygame.image.load("virus_amar_1.png")

JAR = pygame.image.load("frasco_1.png")

######
WINNING = pygame.image.load("win.png")
LOSING = pygame.image.load("lose.png")
NEW_GAME = pygame.image.load("new_game.png")
PAUSE = pygame.image.load("pause.png")
####
VIRUS_LEV_SELEC  = pygame.image.load("virus_level_select.png")
VIRUS_LEV_UNSELEC = pygame.image.load("virus_level_unselec.png")
SPEED_SELEC = pygame.image.load("speed_select.png")
SPEED_UNSELEC = pygame.image.load("speed_unselec.png")
LOW =pygame.image.load("low.png")
MED = pygame.image.load("med.png")
HIGH =pygame.image.load("hi.png") 
SELECTOR = pygame.image.load("selector.png")

MENU = pygame.image.load("menu.png")
INSTRC_MENU = pygame.image.load("instructions_menu.png")
CAPA =pygame.image.load("capa.png")

MARIO = pygame.image.load("mario.png")
#######score
#ficheiro com highscore
if os.path.exists('highscore.txt'):
    open('highscore.txt')
    with open('highscore.txt', "r") as f:
        highscore = int(f.read())
else:
    highscore = 0
# score
score = 0

 ####matrizes iniciais
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
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
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
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
]
#######mapeamento das imagens segundo matrizes
COLORS = {(1, 'u'): UP_1, (2, 'u'): UP_2, (3, 'u'): UP_3, (4, 'u'): UP_4, 
          (1, 'd'): DOWN_1, (2, 'd'): DOWN_2, (3, 'd'): DOWN_3, (4, 'd'): DOWN_4,
          (1, 'r'): RIGHT_1, (2, 'r'): RIGHT_2, (3, 'r'): RIGHT_3, (4, 'r'): RIGHT_4,
          (1, 'l'): LEFT_1, (2, 'l'): LEFT_2, (3, 'l'): LEFT_3, (4, 'l'): LEFT_4,
          (1, 0): SING_1, (2, 0): SING_2, (3, 0): SING_3, (4, 0): SING_4, 
          (1, 'v'): VIRUS_1, (2, 'v'): VIRUS_2, (3, 'v'): VIRUS_3, (4, 'v'): VIRUS_4}

#####mapeamento da matriz para ecrã
TILE_WIDTH = 50
GRID_WIDTH = len(matrix[0])
GRID_HEIGHT = len(matrix)
MARGIN_LEFT = 0
MARGIN_TOP = 0

##### variáveis relógio
fall_time = 1000  # ms
DESLOC_TIME = 300 #ms 

last_fall_time = 0
last_desloc_time = 0

###Comprimido
######## estado inicial do comprimido
player_row_1 = 0
player_col_1 = 0
player_row_2 = 0
player_col_2 = 1
player_color_1 = random.randrange(1, 4+1)
player_color_2 = random.randrange(1, 4+1)
player_state_1 = "l"
player_state_2 = "r"
######### Próximo comprimido
next_player_color_1 = random.randrange(1, 4+1)
next_player_color_2 = random.randrange(1, 4+1)
###### estado inicial de queda 
n_virus = 8*4
all_changes = []
changing_virus = False

#verificar se alguma peça está a ser deslocada
desloc = False
next_same_row = True
next_same_col = True

##### estado das fases do jogo
playing = False
menu_selec = False
win = False
lose = False
pause = False
capa = True

#estado do seletor
virus_selection = True
v_s_l = True
v_s_m = False
v_s_h = False
speed_selection = False
s_p_l = True
s_p_m = False
s_p_h = False

##### TEXTO
# pygame.font.get_fonts()
font = pygame.font.SysFont('arial', 18) 
clock = pygame.time.Clock()

####
change_matrix = False

while running:
    dt = clock.tick(30)
    
    # eventos
    down_pressed = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if capa==True:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    menu_selec = True
                    capa = False
                    print(menu_selec)
        if menu_selec:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    menu_selec = not menu_selec
                    change_matrix = True
                if event.key == pygame.K_ESCAPE: #reset highscore
                    highscore = 0
                    with open('highscore.txt', 'w') as file:
                        file.write(str(highscore))
                if event.key == pygame.K_UP:
                    if speed_selection:
                        virus_selection = True
                        speed_selection = False
                if event.key == pygame.K_DOWN:
                    if virus_selection:
                        speed_selection = True
                        virus_selection = False
                if event.key == pygame.K_LEFT:
                    if virus_selection:
                        if v_s_m:
                            v_s_l = True
                            v_s_m = False
                        if v_s_h:
                            v_s_m = True
                            v_s_h = False
                    if speed_selection:
                         if s_p_m:
                            s_p_l = True
                            s_p_m = False
                         if s_p_h:
                            s_p_m = True
                            s_p_h = False
                       
                    
                if event.key == pygame.K_RIGHT:
                    if virus_selection:
                         if v_s_m:
                            v_s_h = True
                            v_s_m = False
                         if v_s_l:
                            v_s_m = True
                            v_s_l = False

                    if speed_selection:
                        if s_p_m:
                            s_p_h = True
                            s_p_m = False
                        if s_p_l:
                            s_p_m = True
                            s_p_l = False
                
        if playing == True:
            if event.type == pygame.KEYDOWN and desloc == False:
                if event.key == pygame.K_RETURN:
                    if lose == True or win == True:
                        ######highscore do file
                        with open('highscore.txt', 'w') as file:
                            file.write(str(highscore))
                        ####matrizes iniciais    
                        matrix =[
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
                                [0,0,0,0,0,0,0,0],
                                [0,0,0,0,0,0,0,0],
                                [0,0,0,0,0,0,0,0],
                                [0,0,0,0,0,0,0,0],
                                ]
                        ########### variáveis relógio
                        last_fall_time = pygame.time.get_ticks()
                        last_desloc_time = 0
                        
                        ######COMPRIMIDO
                        ###### estado inicial do comprimido
                        player_row_1 = 0
                        player_col_1 = 0
                        player_row_2 = 0
                        player_col_2 = 1
                        player_color_1 = random.randrange(1, 4+1)
                        player_color_2 = random.randrange(1, 4+1)
                        player_state_1 = "l"
                        player_state_2 = "r"
                        ######próximo comprimido
                        next_player_color_1 = random.randrange(1, 4+1)
                        next_player_color_2 = random.randrange(1, 4+1)
                        
                        ###### estado inicial de queda 
                        n_virus = 8*4
                        all_changes = []
                        changing_virus = False
                        
                        #verificar se alguma peça está a ser deslocada
                        desloc = False
                        next_same_row = True
                        next_same_col = True

                        ##### estado das fases do jogo
                        playing = False
                        menu_selec = True
                        win = False
                        lose = False
                        pause = False
                        #### estado do seletor
                        #estado do seletor
                        virus_selection = True
                        v_s_l = True
                        v_s_m = False
                        v_s_h = False
                        speed_selection = False
                        s_p_l = True
                        s_p_m = False
                        s_p_h = False
                        change_matrix = False

                        score = 0                
                if event.key == pygame.K_ESCAPE:
                    pause = not pause
                if event.key == pygame.K_LEFT and (player_col_1>=0 and player_col_2>=0) and pause == False:
                    if player_col_1 > 0 and player_col_2 > 0 and matrix[player_row_1][player_col_1 -1] == matrix[player_row_2][player_col_2 -1] == 0:
                        player_col_1 -= 1
                        player_col_2 -= 1
                if event.key == pygame.K_RIGHT and (player_col_1<=6 and player_col_2<=6) and pause == False:
                    if player_col_1 < len(matrix[0]) and player_col_2 < len(matrix[0]) and matrix[player_row_1][player_col_1 +1] == matrix[player_row_2][player_col_2 +1] == 0:
                        player_col_1 += 1
                        player_col_2 += 1
                if event.key == pygame.K_DOWN:
                    down_pressed = True
                #rodar 
                if event.key == pygame.K_SPACE and pause == False:
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
    #lógica de janelas
    if change_matrix:
        if v_s_l:
            n_virus = 8 
            for i in range(8):
                matrix[13][i] = random.randrange(1, 4+1)
                virus_pill[13][i] = "v"
                matrix[12][i] = random.randrange(1, 4+1)
                virus_pill[12][i] = "v"
        if v_s_m:
            n_virus = 8 
            for i in range(8):
                matrix[11][i] = random.randrange(1, 4+1)
                virus_pill[11][i] = "v"
                matrix[13][i] = random.randrange(1, 4+1)
                virus_pill[13][i] = "v"
                matrix[12][i] = random.randrange(1, 4+1)
                virus_pill[12][i] = "v"
        if v_s_h:
            n_virus = 8 
            for i in range(8):
                matrix[11][i] = random.randrange(1, 4+1)
                virus_pill[11][i] = "v"
                matrix[10][i] = random.randrange(1, 4+1)
                virus_pill[10][i] = "v"
                matrix[13][i] = random.randrange(1, 4+1)
                virus_pill[13][i] = "v"
                matrix[12][i] = random.randrange(1, 4+1)
                virus_pill[12][i] = "v"
                matrix[9][i] = random.randrange(1, 4+1)
                virus_pill[9][i] = "v"
        if s_p_l:
            fall_time = 2000
        if s_p_m:
            fall_time = 1000
        if s_p_h:
            fall_time = 500
        playing = True
        change_matrix = False
    # movimento
    if playing == True:
        if desloc == False and pause == False:
            if ((pygame.time.get_ticks() - last_fall_time) > fall_time or down_pressed):
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
        elif desloc == True and pause == False:
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
                if matrix[row][col] == matrix[row][col+1] == matrix[row][col+2] == matrix[row][col+3] != 0 and (virus_pill[row][col] != "v" or virus_pill[row][col+1] != "v" or virus_pill[row][col+2] != "v" or virus_pill[row][col+3] != "v"):
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
                if matrix[row][col] == matrix[row+1][col] == matrix[row+2][col] == matrix[row+3][col] != 0 and (virus_pill[row][col] != "v" or virus_pill[row+1][col] != "v" or virus_pill[row+2][col] != "v" or virus_pill[row+3][col] != "v"):
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
            score = score + 10
            if score > highscore:
                highscore = score
            
        next_same_row = True
        next_same_col = True
        all_changes = []
                
    # deslocamento se nada tiver em baixo
    #atualização de ligações
    for col in range(8):
        for row in range(14):
            #teste tem a da direita (quebra de ligações)
            if col < 7:
                if virus_pill[row][col] == "l" and virus_pill[row][col+1] != "r":
                    virus_pill[row][col] = 0
            #teste tem a de baixo (quebra de ligações)
            if row < 13:
                if virus_pill[row][col] == "u" and virus_pill[row+1][col] != "d":
                    virus_pill[row][col] = 0
            #teste tem a da esquerda (quebra de ligações)
            if col > 0:
                if virus_pill[row][col] == "r" and virus_pill[row][col-1] != "l":
                    virus_pill[row][col] = 0
            #teste tem a de cima (quebra de ligações)
            if row > 0:
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
    n_virus = 0
    if win == False:
        for col in range(8): 
            for row in range(14):#(evita o out of range)       
                if virus_pill[row][col] == "v":
                    n_virus = n_virus +1
                if matrix[0][col] != 0:
                    lose = True
    if n_virus == 0 and menu_selec == False and change_matrix== False and capa == False:
        win = True
                
    ####################################################################
    # desenhar
    screen.fill((0, 0, 0))

    if capa == True:
        screen.blit(CAPA, (0,0))
    if menu_selec == True:
        #
        screen.blit(MENU, (100 +50+20, 20))
        screen.blit(INSTRC_MENU, (300-5, 700))
        screen.blit(HIGH, (600,270+30))
        screen.blit(MED, (340, 270+30))
        screen.blit(LOW, (80,270+30))
        screen.blit(HIGH, (600,270+320))
        screen.blit(MED, (340, 270+320))
        screen.blit(LOW, (80,270+320))
        if virus_selection:
            screen.blit(VIRUS_LEV_SELEC, (20,70+50))
        else:
            screen.blit(VIRUS_LEV_UNSELEC, (20,70+50))
            
        if speed_selection:
            screen.blit(SPEED_SELEC, (10,420))
        else:
            screen.blit(SPEED_UNSELEC, (10,420))
        if v_s_h: 
            screen.blit(SELECTOR, (600+35,260))
        if v_s_m: 
            screen.blit(SELECTOR, (340+35,260))
        if v_s_l: 
            screen.blit(SELECTOR, (80+35-5,260))
        if s_p_h:
            screen.blit(SELECTOR, (600+35,560))
        if s_p_m:
            screen.blit(SELECTOR, (340+35,560))
        if s_p_l:
            screen.blit(SELECTOR, (80+35-5,560))

    if playing == True:
        if win == False and lose== False:
            screen.blit(JAR, (20,70 + 50))
            screen.blit(MARIO, (450+75, 375+100+50))
            for col in range(8):
                for row in range(14):
                    if matrix[row][col] == 0: continue
                    x = col*TILE_WIDTH+MARGIN_LEFT + 100 - 12
                    y = row*TILE_WIDTH+MARGIN_TOP + 80
                    screen.blit(COLORS[(matrix[row][col], virus_pill[row][col])],(x+2, y+2))
                    text = font.render('Highscore: ' + str(highscore), True, (255, 255, 255))
                    screen.blit(text, (600, 200))
                    text = font.render('Score: ' + str(score), True, (255, 255, 255))
                    screen.blit(text, (600, 220))
            #desenhar primeiro círculo
            x = player_col_1*TILE_WIDTH+MARGIN_LEFT + 100 - 12
            y = player_row_1*TILE_WIDTH+MARGIN_TOP  + 80
        
            screen.blit(COLORS[(player_color_1, player_state_1)], (x+2, y+2))
            #desenhar segundo círculo
            x = (player_col_2)*TILE_WIDTH+MARGIN_LEFT + 100 -12
            y = player_row_2 *TILE_WIDTH+MARGIN_TOP + 80
            screen.blit(COLORS[(player_color_2, player_state_2)], (x+2, y+2))
        
            # NEXT
            x = MARGIN_LEFT + len(matrix[0])*TILE_WIDTH + 100 - 11
            y = MARGIN_TOP + 10
            screen.blit(COLORS[(next_player_color_1, "l")], (x+2, y+2, TILE_WIDTH-4, TILE_WIDTH-4))
            #desenhar segundo círculo
            x = MARGIN_LEFT + len(matrix[0])*TILE_WIDTH + 10 + TILE_WIDTH +80
            screen.blit(COLORS[(next_player_color_2, "r")], (x+2, y+2, TILE_WIDTH-4, TILE_WIDTH-4))
        
        if win == True:
            screen.blit(WINNING, (170, 250))
            screen.blit(NEW_GAME, (290, 420))
        if lose == True:
            screen.blit(LOSING, (180, 250))
            screen.blit(NEW_GAME, (290, 420))
        if pause:
            pygame.draw.rect(screen, (0, 0 ,0), (0, 0, 800, 790))
            screen.blit(PAUSE, (290, 300))
    pygame.display.flip()

with open('highscore.txt', 'w') as file:
    file.write(str(highscore))
pygame.quit()