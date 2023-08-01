import pygame
from pygame.locals import *

pygame.init()

SCREEN_WIDTH = 300
SCREEN_HEIGHT = 300

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption('TIC TAC TOE')
run = True

# define variables
line_width = 6
clicked = False
markers = []
player = 1
pos = []

# define colours
green = (0,255,0)
red = (255,0,0)


for i in range(3):
    row = [0] * 3
    markers.append(row)

print(f'this is the markers!: {markers}')
print('sorry: ', markers[0][1])


def draw_grid():
    bg = (255, 255, 200)
    screen.fill(bg)
    grid = (50,50,50)
    for x in range(1,3):
        pygame.draw.line(screen, grid, (0, x * 100), (SCREEN_WIDTH, x*100), line_width)
        pygame.draw.line(screen, grid, (x * 100, 0), (x*100, SCREEN_HEIGHT), line_width)

def draw_markers():
    x_pos = 0
    for x in markers:
        y_pos = 0
        for y in x:
            if y == 1:
                pygame.draw.line(screen, green, (x_pos *100 + 15, y_pos * 100 + 15), (x_pos * 100 + 85, y_pos * 100 + 85), line_width)
                pygame.draw.line(screen, green, (x_pos *100 + 15, y_pos * 100 + 85), (x_pos * 100 + 85, y_pos * 100 + 15), line_width)
            if y == -1:
                pygame.draw.circle(screen, red, (x_pos * 100 + 50, y_pos * 100 + 50), 38, line_width)
            y_pos +=1
        x_pos +=1



while run:
    draw_grid()
    draw_markers()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN and clicked == False:
            clicked = True
        if event.type == pygame.MOUSEBUTTONUP and clicked == True:
            clicked = False
            pos = pygame.mouse.get_pos()
            cell_x = pos[0]
            cell_y = pos[1]
            if markers[cell_x // 100][cell_y // 100] == 0:
                print(f'and what is this: {markers[cell_x // 100][cell_y // 100]}')
                print(f'alright now what is pos than: {cell_x}and y {cell_y}')
                print(f'what the hell is: {markers} and player {player}')
                markers[cell_x // 100][cell_y // 100] = player
                player *= -1
                print(f'marker is same: {markers} and player is {player}')




    pygame.display.update()

pygame.quit()
