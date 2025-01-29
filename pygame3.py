import pygame
from pygame.locals import *
from random import randint

pygame.init()

WIDTH = 600
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Collision Detection")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        if event.type == KEYUP:
            if event.key == K_ESCAPE:
                running = False
    
pygame.quit()

