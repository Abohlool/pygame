import pygame
from pygame.locals import *

pygame.init()

WIDTH = 600
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Animation")



running = True
while (running):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


pygame.quit