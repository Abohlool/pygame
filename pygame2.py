import pygame
from pygame.locals import *
from random import randint, choice

pygame.init()

WIDTH = 600
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Animation")

# direction constants
DOWNLEFT = "downleft"
DOWNRIGHT = "downright"
UPLEFT = "upleft"
UPRIGHT = "upright"

velocity = 5


running = True
while (running):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        if event.type == KEYUP:
            if event.key == K_ESCAPE:
                running = False
                
        


pygame.quit