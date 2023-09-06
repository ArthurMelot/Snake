import pygame
import random

pygame.init()
nrow = 10
ncol = 10
tile_size = 32
up_border = 100
border = 16
width = 2*border+tile_size*ncol
height = up_border + tile_size*nrow
window = pygame.display.set_mode((width,height))

#Colors
black = pygame.Color(0,0,0)
white = pygame.Color(255,255,255)
red = pygame.Color(255,0,0)
green = pygame.Color(0,255,0)
blue = pygame.Color(0,0,255)