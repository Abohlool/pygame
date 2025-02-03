import pygame
from pygame.locals import *
from random import randint

pygame.init()
clock = pygame.time.Clock()

WIDTH = 400
HEIGHT = 400

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("media")

moveDown = False
moveUp = False
moveRight = False
moveLeft = False
VELOCITY = 10

player = pygame.Rect(300, 100, 40, 40)
playerImg = pygame.image.load("player.png")
playerImgFitted = pygame.transform.scale(playerImg, (player.width, player.height))
cherryImg = pygame.image.load("cherry.png")

pickUpSound = pygame.mixer.Sound("pickup.wav")
pygame.mixer.music.load("background.mid")
pygame.mixer.music.play(-1, 0.0)
musicPlaying = True

counter = 0
NEWPOINT = 40
SIZE = 20

points = list()
for _ in range(20):
    points.append(pygame.Rect(randint(0, WIDTH - SIZE), randint(0, HEIGHT - SIZE), SIZE, SIZE))

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
            
            if event.key in [K_UP, K_w]:
                moveUp = False
                    
            if event.key in [K_LEFT, K_a]:
                moveLeft = False
                
            if event.key in [K_DOWN, K_s]:               
                moveDown = False
                
            if event.key in [K_RIGHT, K_d]:               
                moveRight = False
                
        if event.type == KEYDOWN:
            if event.key in [K_UP, K_w]:
                moveUp = True
                moveDown = False
            
            if event.key in [K_LEFT, K_a]:
                moveLeft = True
                moveRight = False
                
            if event.key in [K_DOWN, K_s]:
                moveDown = True
                moveUp = False
                
            if event.key in [K_RIGHT, K_d]:
                moveRight = True
                moveLeft = False
    
    counter += 1
    if counter >= NEWPOINT:
        counter = 0
        points.append(pygame.Rect(randint(0, WIDTH - SIZE), randint(0, HEIGHT - SIZE), SIZE, SIZE))
                
    screen.fill(0xFFFFFF)

    if moveDown and player.bottom < HEIGHT:
        player.bottom += VELOCITY
    if moveUp and player.top > 0:
        player.top -= VELOCITY
    if moveRight and player.right < WIDTH:
        player.right += VELOCITY
    if moveLeft and player.left > 0:
        player.left -= VELOCITY
        
    screen.blit(playerImgFitted, player)

    for point in points[:]:
        if player.colliderect(point):
            points.remove(point)
            player.width += 2
            player.height += 2
            player = pygame.Rect(player.left, player.top, player.width, player.height)
            playerImgFitted = pygame.transform.scale(playerImg, (player.width, player.height))
            
            if musicPlaying:
                pickUpSound.play()
                
            
    for point in points:
        screen.blit(cherryImg, point)

    pygame.display.update()
    clock.tick(60)
    
pygame.quit()