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
