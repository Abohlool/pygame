import pygame
from pygame.locals import *
from random import randint

pygame.init()
pygame.time.Clock()

WIDTH = 400
HEIGHT = 400 

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("enemy")

player = pygame.Rect(300, 100, 40, 40)
playerImg = pygame.image.load("src8/player.png")
playerImgFitted = pygame.transform.scale(playerImg, (player.width, player.height))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runnning = False

pygame.quit()
