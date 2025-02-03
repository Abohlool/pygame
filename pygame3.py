import pygame
from pygame.locals import *
from random import randint

pygame.init()
clock = pygame.time.Clock()

WIDTH = 400
HEIGHT = 400

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Collision Detection")

counter = 0
NEWPOINT = 40
SIZE = 20

player = pygame.Rect(randint(0, WIDTH - 50), randint(0, HEIGHT -50), 50, 50)
PLAYERCOLOUR = (randint(5, 250), randint(5, 250), randint(5, 250))

    
points = list()
for _ in range(20):
    points.append({"rect": pygame.Rect(randint(0, WIDTH - SIZE), randint(0, HEIGHT - SIZE), SIZE, SIZE), 
                   "colour": (randint(5, 250), randint(5, 250), randint(5, 250))})

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

        if event.type == KEYDOWN:
            if event.key == K_w or event.key == K_UP:
                moveUp = True
                moveDown = False
                
            if event.key == K_s or event.key == K_DOWN:
                moveup = False
                moveDown = True
                
            if event.key == K_d or event.key == K_RIGHT:
                moveRight = True
                moveLeft = False
            
            if event.key == K_a or event.key == K_LEFT:
                moveRight = False
                moveLeft = True
                
            if event.key == K_x:
                player.top = randint(0, HEIGHT - player.height)
                player.left = randint(0, WIDTH - player.width)
            
        if event.type == KEYUP:
            if event.type == KEYUP:
                if event.key == K_ESCAPE:
                    running = False
                
            if event.key == K_w or event.key == K_UP:
                moveUp = False

            if event.key == K_d or event.key == K_DOWN:
                moveDown = False

            if event.key == K_d or event.key == K_RIGHT:
                moveRight = False

            if event.key == K_a or event.key == K_LEFT: 
                moveLeft = False
                
        if event.type == MOUSEBUTTONUP:
            points.append(pygame.Rect(event.pos[0], event.pos[1], SIZE, SIZE))
        
    counter += 1
    if counter >= NEWPOINT:
        counter = 0
        points.append({"rect": pygame.Rect(randint(0, WIDTH - SIZE), randint(0, HEIGHT - SIZE), SIZE, SIZE), 
                   "colour": (randint(5, 250), randint(5, 250), randint(5, 250))})
        
    screen.fill(0xFFFFFF)

    if moveDown and player.bottom < HEIGHT:
        player.bottom += velocity

    if moveUp and player.top > 0:
        player.top -= velocity

    if moveRight and player.right < WIDTH:
        player.right += velocity

    if moveLeft and player.left > 0:
        player.left -= velocity
    
    pygame.draw.rect(screen, PLAYERCOLOUR, player)
    
    for newPoint in points[:]:
        if player.colliderect(newPoint["rect"]):
            points.remove(newPoint)
    
    for point in points:
        pygame.draw.rect(screen, point["colour"], point["rect"])

    pygame.display.update() 
    clock.tick(60)
    
pygame.quit()
