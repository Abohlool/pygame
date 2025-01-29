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
    
        if event.type == KEYDOWN:
            if event.key in [K_w, K_UP]:
                moveUp = True
                moveDown = False
                
            elif event.key in [K_s, K_DOWN]:
                moveup = False
                moveDown = True
                
            if event.key in [K_d, K_RIGHT]:
                moveRight = True
                moveLeft = False
            
            elif event.key in [K_a, K_LEFT]:
                moveRight = False
                moveLeft = True
                
            if event.key == K_x:
                player.top = randint(0, HEIGHT - player.height)
                player.left = randint(0, WIDTH - player.width)
            
        if event.type == KEYUP:
            if event.key in [K_w, K_UP]:
                moveUp = False

            elif event.key in [K_d, K_DOWN]:
                moveDown = False

            if event.key in [K_d, K_RIGHT]:
                moveRight = False

            elif event.key in [K_a, K_LEFT]: 
                moveLeft = False
                
        if event.type == MOUSEBUTTONUP:
            points.append(pygame.Rect(event.pos[0], event.pos[1], SIZE, SIZE))
        
        counter += 1
        if counter >= NEWPOINT:
            counter = 0
            points.append(pygame.Rect(randint(0, WIDTH - SIZE), randint(0, HEIGHT - SIZE), SIZE, SIZE))
            
            
pygame.quit()

