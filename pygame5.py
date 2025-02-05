import pygame, sys
from pygame.locals import *
from random import randint

WIDTH = 600
HEIGHT = 600
FPS = 60
ENEMYRATE = 9
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
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()

            if event.type == KEYUP:
                if event.key == K_ESCAPE:
                    terminate()

                return 
    
def collision(player, enemies) -> bool:
    for enemy in enemies:
        if player.colliderect(enemy["rect"]):
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
pygame.display.set_caption("Dodger")
pygame.mouse.set_visible(False)

font = pygame.font.SysFont(None, 48)

gameOverSound = pygame.mixer.Sound("src8/gameover.wav")
pygame.mixer.music.load("src8/background.mid")

playerImg = pygame.image.load("src8/player.png")
playerRect = playerImg.get_rect()
enemyImg = pygame.image.load("src8/baddie.png")

screen.fill(0xFFFFFF)
drawText("Dodger", font, screen, WIDTH / 3, HEIGHT / 3)
drawText("Press a key to start.", font, screen, (WIDTH / 3) - 30, (HEIGHT / 3) + 50)
pygame.display.update()
wait()

topScore = 0
while True:
    enemies = list()
    score = 0
    playerRect.topleft = (WIDTH / 2, HEIGHT - 50)
    moveLeft = moveRight = moveUp = moveDown = False
    enemyCounter = 0
    pygame.mixer.music.play(-1, 0.0)
    while True:
        score += 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()

            if event.type == KEYDOWN:
                if event.key in [K_w, K_UP]:
                    moveUp = True
                    moveDown = False

                if event.key in [K_a, K_LEFT]:
                    moveLeft = True
                    moveRight = False
                
                if event.key in [K_s, K_DOWN]:
                    moveDown = True
                    moveUp = False
                
                if event.key in [K_d, K_RIGHT]:
                    moveRight = True
                    moveLeft = False
                
            if event.type == KEYUP:
                if event.key == K_ESCAPE:
                    terminate()
                    
                if event.key in [K_w, K_UP]:
                    moveUp = False
                
                if event.key in [K_a, K_LEFT]:
                    moveLeft = False
                    
                if event.key in [K_s, K_DOWN]:
                    moveDown = False
                
                if event.key in [K_d, K_RIGHT]:
                    moveRight = False
                
            if event.type == MOUSEMOTION:
                playerRect.center = (event.pos[0], event.pos[1])
        
        enemyCounter += 1
        if enemyCounter >= ENEMYRATE:
            enemyCounter = 0
            size = randint(MINSIZE, MAXSIZE)
            newEnemy = {
                        "rect": pygame.Rect(randint(0, WIDTH - size), 0 - size, size, size),
                        "speed": randint(MINSPEED, MAXSPEED),
                        "img": pygame.transform.scale(enemyImg, (size, size))
                        }
            enemies.append(newEnemy)
            
        if moveUp and playerRect.top > 0:
            playerRect.move_ip(0, -1 * PLAYERSPEED)
        
        if moveLeft and playerRect.left > 0:
            playerRect.move_ip(-1 * PLAYERSPEED, 0)
            
        if moveDown and playerRect.bottom < HEIGHT:
            playerRect.move_ip(0, PLAYERSPEED)
        
        if moveRight and playerRect.right < WIDTH:
            playerRect.move_ip(PLAYERSPEED, 0)
        
        for enemy in enemies:
            enemy["rect"].move_ip(0, enemy["speed"])

        for enemy in enemies[:]:
            if enemy["rect"].top > HEIGHT:
                enemies.remove(enemy)
        
        screen.fill(0xFFFFFF)
        
        drawText(f"Score: {score}", font, screen, 10, 0)
        drawText(f"Top Score: {topScore}", font, screen, 10, 40)

        screen.blit(playerImg, playerRect)

        for enemy in enemies:
            screen.blit(enemy["img"], enemy["rect"])

        pygame.display.update()
        
        if collision(playerRect, enemies):
            if score > topScore:
                topScore = score
            break
        
        clock.tick(FPS)

    pygame.mixer.music.stop()
    gameOverSound.play()
    
    drawText("GAME OVER", font, screen, (WIDTH / 3),(HEIGHT / 3))
    drawText("Press a key to play again.", font, screen, (WIDTH / 3) - 80, (HEIGHT / 3) + 50)
    pygame.display.update()
    wait()
    
    gameOverSound.stop()
    


