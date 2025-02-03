import pygame
from pygame.locals import *
from random import randint

pygame.init()
pygame.time.Clock()

WIDTH = 400
HEIGHT = 400 

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("enemy")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runnning = False

pygame.quit()
