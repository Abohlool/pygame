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

pygame.init()

def terminate():
    ...
    
def wait():
    ...
    
def collision():
    ...
    
def txt():
    ...

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminate()
            