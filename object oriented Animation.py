import pygame
import random           #in terminal pip install pygame
#create color constants


WHITE = (255, 255, 255)
RED = (87, 9, 9)
GREEN = (12, 148, 37)
BLUE = (2, 0, 94)
BLACK = (0, 0, 0)
PURPLE = (28, 4, 54)
SAND_YELLOW = (76, 70, 50)

#width by height
FPS = 60
DISPLAYWIDTH = 700
DISPLAYHEIGHT = 500
pygame.init()
screen = pygame.display.set_mode((DISPLAYWIDTH, DISPLAYHEIGHT))

class Beach():

    def __init__(self,x,y,width,height,color1,screen):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color1 = color1
        self.screen = screen

    def draw_beach(self):
        pygame.draw.rect(self.screen,self.color1,[self.x,self.y,self.width,self.height])






beach = Beach(0,300,900,600,SAND_YELLOW,screen)

pygame.display.set_caption("my Pygame animation")

clock = pygame.time.Clock()

running = True



while running:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False
    screen.fill(BLUE)


    beach.draw_beach()

    pygame.display.flip()

    clock.tick(FPS)

pygame.quit()
