import pygame
from snake import SCREEN_HEIGHT, SCREEN_WIDTH, BOARD_SIZE
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

background = pygame.Surface(size= (400, 400))
width = SCREEN_WIDTH//BOARD_SIZE
height = SCREEN_HEIGHT//BOARD_SIZE
checker_pattern = 0
for y in range(BOARD_SIZE):
    for x in range(BOARD_SIZE):
        square = pygame.Rect()
        square.topleft = (x*width, y*height)
        square.height = height
        square.width = width
        if x % 2 == checker_pattern % 2:
            color = "chartreuse3"
        else:
            color = "chartreuse2"
        pygame.draw.rect(background, color, square)
    checker_pattern += 1

BACKGROUND_IMAGE = background
rect = pygame.surface.Surface.get_rect(BACKGROUND_IMAGE)
rect.topleft = (0, 0)
BACKGROUND_RECT = rect
