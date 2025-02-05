import pygame, sys
from pygame.locals import *
from random import randint

WIDTH = 400
HEIGHT = 400
FPS = 60
MAXSIZE = 40
MINSIZE = 10
MINSPEED = 1
MAXSPEED = 8
PLAYERSPEED = 5

def terminate() -> None:
    pygame.quit()
    sys.exit()
    
def wait() -> None:
    while True:
        for event in pygame.evennt.get():
            if event.type == pygame.QUIT:
                terminate()

            if event.type == KEYUP:
                if event.key == K_ESCAPE:
                    terminate()

                return 
    
def collision(player, enemies) -> bool:
    for enemy in enemies:
        if player.coliderect(enemy):
            return True

    return False
    
def drawText(txt: str, font, screen, x: int, y: int) -> None:
    text = font.render(txt, True, 0x000000)
    textRect = text.get_rect()
    textRect.topleft = (x, y)
    screen.blit(text, textRect)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminate()
            