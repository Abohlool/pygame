import pygame, random
from pygame.locals import *

pygame.init()

# Constants
WIDTH: int = 1100
HEIGHT: int = 600


# Display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chrome Dino")

# Images
runningImg = [pygame.image.load("src/DinoRun1.png"),
              pygame.image.load("src/DinoRun2.png")]

jumpingImg = pygame.image.load("src/DinoJump.png")

duckingImg = [pygame.image.load("src/DinoDuck1.png"),
              pygame.image.load("src/DinoDuck2.png")]

smallCactai = [pygame.image.load("src/SmallCactus1.png"),
               pygame.image.load("src/SmallCactus2.png"),
               pygame.image.load("src/SmallCactus3.png")]

largeCactai = [pygame.image.load("src/LargeCactus1.png"),
               pygame.image.load("src/LargeCactus2.png"),
               pygame.image.load("src/LargeCactus3.png")]

birdImg = [pygame.image.load("src/Bird1.png"),
            pygame.image.load("src/Bird2.png")]

cloudImg = pygame.image.load("src/Cloud.png")

trackImg = pygame.image.load("src/Track.png")


# Dino class
class Dino:
    x_pos: int = 80
    y_pos: int = 310
    y_pos_duck: int = 340
    jump_velocity: float = 8.5

    def __init__(self):
        self.duckImg = duckingImg
        self.jumpImg = jumpingImg
        self.runImg = runningImg
        
        self.ducking = False
        self.running = True
        self.jumping = False
        
        self.step = 0
        self.jumpVelocity = self.jump_velocity
        self.image = self.runImg[0]
        self.dinoRect = self.image.get_rect()
        self.dinoRect.topleft = (self.x_pos, self.y_pos)
        
    
    def update(self):
        if self.ducking:
            self.duck()
            
        if self.jumping:
            self.jump()
            
        if self.running:
            self.run()
            
        if self.step >= 10:
            self.step = 0
    
    def jump(self):
        self.image = self.jumpImg
        if self.jumping:
            self.dino_rect.y -= self.jump_velocity * 4
            self.jump_velocity -= 0.8
    
        if self.jump_velocity < - self.jumpVelocity:
            self.dino_jump = False
            self.jump_velocity = self.jumpVelocity

    
    def duck(self):
        self.image = self.duckImg[self.step // 5]
        self.dinoRect = self.image.get_rect()
        self.dinoRect.topleft = (self.x_pos, self.y_pos_duck)
        self.step += 1

    
    def run(self):
        self.image = self.run_img[self.step // 5]
        self.dinoRect = self.image.get_rect()
        self.dinoRect.topleft = (self.x_pos, self.y_pos)
        self.step += 1

    def draw(self):
        screen.blit(self.image, self.dinoRect.topleft)
    
class cloud:
    def __init__(self):
        pass
    
    def update(self):
        pass
    
    def draw(seld):
        pass
    
class Obstacle:
    def __init__(self):
        pass
    
    def update(self):
        pass
    
    def fraw(self):
        pass


        
    