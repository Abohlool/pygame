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
    jump_velocity: float = .5

    def __init__(self):
        pass
    
    def update(self):
        pass
    
    def jump(self):
        pass
    
    def duck(self):
        pass
    
    def run(self):
        pass

    def draw(self):
        pass
    
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


        
    