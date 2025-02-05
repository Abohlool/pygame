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

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Doger")
pygame.mouse.set_visible(False)

font = pygame.font.SysFont(None, 48)

gameOverSound = pygame.mixer.Sound("src8/gameover.wav")
pygame.mixer.music.load("src8/background.mid")

playerImg = pygame.image.load("src8/player.png")
playerRect = playerImg.get_rect()
enemyImg = pygame.image.load("src8/baddie.png")
enemySmall = pygame.transform.scale(enemyImg, (MINSIZE, MINSIZE))
enemyBig = pygame.transform.scale(enemyImg, (MAXSIZE, MAXSIZE))

screen.fill(0xFFFFFF)
drawText("Doger", font, screen, WIDTH / 3, HEIGHT / 3)
drawText("Press a key to start.", font, screen, (WIDTH / 3) - 30, (HEIGHT / 3) + 50)
pygame.display.update()
wait()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminate()
            