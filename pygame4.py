import pygame
from pygame.locals import *

pygame.init()
clock = pygame.time.Clock()

WIDTH = 500
HEIGHT = 500

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("media")

player = pygame.Rect(300, 100, 40, 40)
playerImg = pygame.image.load("player.png")
playerImgFitted = pygame.transform.scale(playerImg, (40, 40))
cherryImg = pygame.image.load("cherry.png")

pickUpSound = pygame.mixer.Sound("pickup.wav")
pygame.mixer.music.load("background.mid")
pygame.mixer.music.play(-1, 0.0)
musicPlaying = True

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == KEYUP:
            if event.key == K_ESCAPE:
                running = False
                
            if event.key == K_m:
                if musicPlaying:
                    pygame.mixer.music.stop()
                    
                else:
                    pygame.mixer.music.play(-1, 0.0)
                    
                musicPlaying = not musicPlaying
                
        screen.fill(0xC7C7C7)
        pygame.display.update()

pygame.quit()