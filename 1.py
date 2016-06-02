import pygame
import random

from pygame.locals import *
from sys import exit
# Initialize the game engine
pygame.init()
def main_zickle(self):


    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    GREY = (200, 200, 200)
    GREEN = (0, 255, 0)

    # Set the height and width of the screen
    # -----------------------------------
    stroki = 10
    stolbiki = 20
    shirina_uacheiki = 20
    visota_uacheiki = 20
    otstup = 3
    shirina_s_otstupom = shirina_uacheiki + otstup
    visota_s_otstupom = visota_uacheiki + otstup

    SIZE = [shirina_s_otstupom*stolbiki+otstup, visota_s_otstupom*stroki+otstup]
    # SIZE = [300, 400]
    # -----------------------------------
    screen = pygame.display.set_mode(SIZE)
    pygame.display.set_caption("Saper")

    clock = pygame.time.Clock()

    # gm = 3
    # gw = 25
    # gh = 25
    # i = 10
    # j = 10
    #
    # grid = []
    # for ii in range(i):
    #     grid.append([])
    #     for jj in range(j):
    #         grid[ii].append(0)
    # Loop until the user clicks the close button.
    done = False

    #-------------------------------------------------
    # stroki = 10
    # stolbiki = 20
    # otstup = 2
    # shirina_s_otstupom = (SIZE[0]-otstup)/stolbiki
    # shirina_uacheiki = shirina_s_otstupom - otstup
    # visota_s_otstupom = (SIZE[1]-otstup)/stroki
    # visota_uacheiki = visota_s_otstupom - otstup
    #-------------------------------------------------

    grid = []
    for stroka in range(stroki):
        grid.append([])
        for stolbik in range(stolbiki):
            grid[stroka].append({"mina":0, "nagata":0, "vokrug":0})


    def set_mina(i,j):
        grid[i][j]["mina"] = 1
        for stroka in range(i-1, i+2):
            for stolbik in range(j-1, j+2):
                if stroka == i and stolbik == j:
                    continue
                if stroka < 0 or stroka > (stroki - 1) or stolbik < 0 or stolbik > (stolbiki - 1):
                    continue
                if grid[stroka][stolbik]["mina"] == 1:
                    continue
                grid[stroka][stolbik]["vokrug"] += 1

    # mina = grid
    for elem in range(20):
        i = random.randint(0, stroki - 1)
        j = random.randint(0, stolbiki - 1)
        print(i,j)
        set_mina(i, j)


    # set up fonts
    basicFont = pygame.font.SysFont(None, 20)

    # set up the text

    def change_grid_status(x, y):
        j = int(x/shirina_s_otstupom)
        i = int(y/visota_s_otstupom)
        if grid[i][j]["nagata"] > 0:
            grid[i][j]["nagata"] = 0
        else:
            grid[i][j]["nagata"] = 1

    color_cell = GREY
    show_text = False
    text = None
    while not done:
        for event in pygame.event.get():   # User did something
            if event.type == pygame.QUIT:  # If user clicked close
                done = True   # Flag that we are done so we exit this loop
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    i, j = event.pos
                    change_grid_status(i, j)


        # Set the screen background
        screen.fill(BLACK)
        # screen.blit(background_image, [0, 0])
        x = 0
        y = 0
        pygame.draw.line(screen,GREEN,[x, y], [x, SIZE[1]], otstup)
        pygame.draw.line(screen,GREEN,[x, y], [SIZE[0], y], otstup)
        pygame.draw.line(screen,GREEN,[SIZE[0], y], [SIZE[0], SIZE[1]], otstup)
        pygame.draw.line(screen,GREEN,[SIZE[0], SIZE[1]], [x, SIZE[1]], otstup)
        for stroka in range(stroki):
            y = stroka*visota_s_otstupom + otstup
            for stolbik in range(stolbiki):
                x = stolbik*shirina_s_otstupom + otstup
                if grid[stroka][stolbik]["nagata"] == 1:
                    if grid[stroka][stolbik]["mina"] == 1:
                        color_cell = RED
                    else:
                        color_cell = WHITE
                        text = basicFont.render(str(grid[stroka][stolbik]["vokrug"]), True, BLACK,WHITE)
                        textRect = text.get_rect()
                        textRect.centerx = x + int(shirina_uacheiki/2)
                        textRect.centery = y + int(visota_uacheiki/2)
                        show_text = True
                else:
                    color_cell = GREY
                    show_text = False
                    text = None
                pygame.draw.rect(screen,color_cell,[x , y, shirina_uacheiki, visota_uacheiki])
                if show_text == True:
                    screen.blit(text, textRect)
        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()
        clock.tick(60)

    # Be IDLE friendly. If you forget this line, the program will 'hang'
    # on exit.
    pygame.quit()

