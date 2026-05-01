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
    "UP": {
        "UP": pygame.image.load("Graphics/body_vertical.png").convert_alpha(),
        "LEFT": pygame.image.load("Graphics/body_bottomleft.png").convert_alpha(),
        "RIGHT": pygame.image.load("Graphics/body_bottomright.png").convert_alpha()
    },
    "DOWN": {
        "DOWN": pygame.image.load("Graphics/body_vertical.png").convert_alpha(),
        "LEFT": pygame.image.load("Graphics/body_topleft.png").convert_alpha(),
        "RIGHT": pygame.image.load("Graphics/body_topright.png").convert_alpha()        
    },
    "LEFT": {
        "UP": pygame.image.load("Graphics/body_topright.png").convert_alpha(),
        "DOWN": pygame.image.load("Graphics/body_bottomright.png").convert_alpha(),
        "LEFT": pygame.image.load("Graphics/body_horizontal.png").convert_alpha()
    },
    "RIGHT": {
        "UP": pygame.image.load("Graphics/body_topleft.png").convert_alpha(),
        "DOWN": pygame.image.load("Graphics/body_bottomleft.png").convert_alpha(),
        "RIGHT": pygame.image.load("Graphics/body_horizontal.png").convert_alpha()        
    }
}