import pygame
from pygame.locals import *

pygame.init()

WIDTH = 500
HEIGHT = 500

screen = pygame.display.set_mode((HEIGHT, WIDTH))
pygame.display.set_caption("First Game")

x = 50
y = 50
width = 40
height = 60
velocity = 5

running = True
while running:
    pygame.time.delay(100)
    pygame.display.update()
    screen.fill(0x220022)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == KEYUP:
            if event.key == K_ESCAPE:
                running = False

            elif event.key in [K_w, K_UP]:
                y -= velocity

            elif event.key in [K_d, K_RIGHT]:
                x += velocity
            
            elif event.key in [K_s, K_DOWN]:
                y += velocity
            
            elif event.key in [K_a, K_LEFT]:
                x -= velocity
                
    
    pygame.draw.rect(screen, 0xFF0000, (x, y, width, height))
pygame.quit()