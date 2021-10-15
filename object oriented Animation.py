import pygame
import random  # in terminal pip install pygame

# create color constants


WHITE = (255, 255, 255)
RED = (87, 9, 9)
GREEN = (12, 148, 37)
BLUE = (2, 0, 94)
BLACK = (0, 0, 0)
PURPLE = (28, 4, 54)
SAND_YELLOW = (255, 255, 102)

# width by height
FPS = 60
DISPLAYWIDTH = 700
DISPLAYHEIGHT = 500
pygame.init()
screen = pygame.display.set_mode((DISPLAYWIDTH, DISPLAYHEIGHT))


class Beach():

    def __init__(self, x, y, width, height, color1, screen):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color1 = color1
        self.screen = screen

    def draw_beach(self):
        pygame.draw.rect(self.screen, self.color1, [self.x, self.y, self.width, self.height])


class Cloud():

    def __init__(self, screen, cloud_color1, cloud_x, cloud_y, cloud_radius):
        self.cloud_x = cloud_x
        self.cloud_y = cloud_y
        self.cloud_color1 = cloud_color1
        self.cloud_radius = cloud_radius
        self.screen = screen

    def draw_Cloud(self):
        pygame.draw.circle(self.screen, self.cloud_color1, [self.cloud_x, self.cloud_y], self.cloud_radius)

    def move_cloud(self):
        self.cloud_x += 5
        if self.cloud_x-3.5*self.cloud_radius > DISPLAYHEIGHT:
            self.cloud_x = -3.5*self.cloud_radius


class Umbrella_stand():
    def __init__(self, screen, umbrella_color, umbrella_x,umbrella_y,umbrella_width,umbrella_height):
        self.screen = screen
        self.umbrella_color = umbrella_color
        self.umbrella_x = umbrella_x
        self.umbrella_y = umbrella_y
        self.umbrella_width = umbrella_width
        self.umbrella_height = umbrella_height

    def draw_ubrella(self):
        pygame.draw.rect(self.screen,self.umbrella_color,[self.umbrella_x,self.umbrella_y,self.umbrella_width,self.umbrella_height])



class Umbrella_top1():
    def __init__(self, screen,umbrella_color1,umbrella1_x,umbrella1_y,umbrella1_width,umbrella1_height):
        self.screen = screen
        self.umbrella_color1 = umbrella_color1
        self.umbrella1_x = umbrella1_x
        self.umbrella1_y = umbrella1_y
        self.umbrella1_width = umbrella1_width
        self.umbrella1_height = umbrella1_height

    def draw_umbrella1(self):
        pygame.draw.rect(self.screen,self.umbrella_color1,[self.umbrella1_x,self.umbrella1_y,self.umbrella1_width,self.umbrella1_height])




beach = Beach(0, 300, 900, 600, SAND_YELLOW, screen)



clouds = [Cloud(screen, WHITE,
                random.randint(0, DISPLAYWIDTH), random.randint(0, int(DISPLAYHEIGHT*.25)),60)
          for x in range(25)]



umbrella = Umbrella_stand(screen,BLACK,350,350,200,50)
umbrealla_top1 = Umbrella_top1(screen,RED,20,350,200,50)



pygame.display.set_caption("my Pygame animation")

clock = pygame.time.Clock()

running = True

while running:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False
    screen.fill(BLUE)

    beach.draw_beach()

    for cloud in clouds:
        cloud.draw_Cloud()
        cloud.move_cloud()

    umbrella.draw_ubrella()
    umbrealla_top1.draw_umbrella1()
    pygame.display.flip()

    clock.tick(FPS)

pygame.quit()
