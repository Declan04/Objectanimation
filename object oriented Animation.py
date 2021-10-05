import pygame
import random           #in terminal pip install pygame
#create color constants


WHITE = (255, 255, 255)
RED = (87, 9, 9)
GREEN = (12, 148, 37)
BLUE = (2, 0, 94)
BLACK = (0, 0, 0)
PURPLE = (28, 4, 54)


#width by height
FPS = 60
DISPLAYWIDTH = 700
DISPLAYHEIGHT = 500
pygame.init()










screen = pygame.display.set_mode((DISPLAYWIDTH, DISPLAYHEIGHT))

pygame.display.set_caption("my Pygame animation")

clock = pygame.time.Clock()

running = True



while running:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False
    screen.fill(PURPLE)




    pygame.display.flip()

    clock.tick(FPS)

pygame.quit()
