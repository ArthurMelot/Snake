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
window = pygame.display.set_mode(width,height)

#Images
empty = pygame.image.load("Images/empty.png")
fruit = pygame.image.load("Images/fruit.png")

head_up = pygame.image.load("Images/head_up.png")
head_right = pygame.transform.rotate(head_up,90)
head_down = pygame.transform.rotate(head_up,180)
head_left = pygame.transform.rotate(head_up,270)

body_vert = pygame.image.load("Images/body_vertical.png")
body_horiz = pygame.transform.rotate(body_vert,90)

tail_up = pygame.image.load("Images/tail_up.png")
tail_right = pygame.transform.rotate(tail_up,270)
tail_down = pygame.transform.rotate(tail_up,180)
tail_left = pygame.transform.rotate(tail_up,90)

turn_UR = pygame.image.load("Images/turn_UR.png")
turn_UL = pygame.transform.rotate(turn_UR,90)
turn_DL = pygame.transform.rotate(turn_UR,180)
turn_DR = pygame.transform.rotate(turn_UR,270)
