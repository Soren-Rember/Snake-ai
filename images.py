import pygame
pygame.display.set_mode((400, 400))

HEAD_IMAGES = {
    "UP": pygame.image.load("Graphics/head_up.png").convert_alpha(),
    "DOWN": pygame.image.load("Graphics/head_down.png").convert_alpha(),
    "LEFT": pygame.image.load("Graphics/head_left.png").convert_alpha(),
    "RIGHT": pygame.image.load("Graphics/head_right.png").convert_alpha()
}

TAIL_IMAGES = {
    "UP": pygame.image.load("Graphics/tail_up.png").convert_alpha(),
    "DOWN": pygame.image.load("Graphics/tail_down.png").convert_alpha(),
    "LEFT": pygame.image.load("Graphics/tail_left.png").convert_alpha(),
    "RIGHT": pygame.image.load("Graphics/tail_right.png").convert_alpha()
}

BODY_IMAGES = {
    
}