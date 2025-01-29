import pygame
from pygame.locals import *
from random import randint

pygame.init()

WIDTH = 600
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Collision Detection")

counter = 0
NEWPOINT = 40
SIZE = 20

player = pygame.Rect(randint(0, WIDTH - 50), randint(0, HEIGHT -50), 50, 50)

points = list()
for _ in range(20):
    points.append(pygame.Rect(randint(0, WIDTH - SIZE), randint(0, HEIGHT - SIZE), SIZE, SIZE))

moveDown = False
moveUp = False
moveLeft = False
moveRight = False
velocity = 5

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        if event.type == KEYUP:
            if event.key == K_ESCAPE:
                running = False
    
pygame.quit()

