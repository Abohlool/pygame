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

dir = [DOWNLEFT, DOWNRIGHT, UPLEFT, UPRIGHT]

velocity = 1
BOXES = 3

def box():
    len = randint(50, 100)
    return {
        "rect": pygame.Rect(randint(0, WIDTH - len), randint(0, HEIGHT - len), len, len),
        "dir": choice(dir),
        "colour": (randint(5, 250), randint(5, 250), randint(5, 250))
            }

boxes = list()

for _ in range(BOXES):
    boxes.append(box())

running = True
while (running):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        if event.type == KEYUP:
            if event.key == K_ESCAPE:
                running = False
                
    for box in boxes:
        if box["rect"].bottom > HEIGHT:
            if box["dir"] == DOWNLEFT:
                box["dir"] = UPLEFT
            
            elif box["dir"] == DOWNRIGHT:
                box["dir"] = UPRIGHT
        
        elif box["rect"].top < 0:
            if box["dir"] == UPLEFT:
                box["dir"] = DOWNLEFT
            
            elif box["dir"] == UPRIGHT:
                box["dir"] = DOWNRIGHT
        
        if box["rect"].left < 0:
            if box["dir"] == DOWNLEFT:
                box["dir"] = DOWNRIGHT
            
            elif box["dir"] == UPLEFT:
                box["dir"] = UPRIGHT
        
        elif box["rect"].right > WIDTH:
            if box["dir"] == DOWNRIGHT:
                box["dir"] = DOWNLEFT
            
            elif box["dir"] == UPRIGHT:
                box["dir"] = UPLEFT
        

        if box["dir"] == DOWNLEFT:
            box["rect"].top += velocity
            box["rect"].left -= velocity
        
        elif box["dir"] == DOWNRIGHT:
            box["rect"].top += velocity
            box["rect"].left += velocity

        elif box["dir"] == UPLEFT:
            box["rect"].top -= velocity
            box["rect"].left -= velocity

        elif box["dir"] == UPRIGHT:
            box["rect"].top -= velocity
            box["rect"].left += velocity
            
        pygame.draw.rect(screen, box["colour"], box["rect"])

    pygame.display.update()
    screen.fill(0xFFFFFF)
    pygame.time.delay(3)
    
        
pygame.quit