import pygame
from direction import Direction
pygame.display.set_mode((400, 400))

body_bottomleft = pygame.image.load("/home/soren/Projects/snake_ai/Graphics/body_bottomleft.png").convert_alpha()
body_bottomright = pygame.image.load("/home/soren/Projects/snake_ai/Graphics/body_bottomright.png").convert_alpha()
body_horizontal = pygame.image.load("/home/soren/Projects/snake_ai/Graphics/body_horizontal.png").convert_alpha()
body_topleft = pygame.image.load("/home/soren/Projects/snake_ai/Graphics/body_topleft.png").convert_alpha()
body_topright = pygame.image.load("/home/soren/Projects/snake_ai/Graphics/body_topright.png").convert_alpha()
body_vertical = pygame.image.load("/home/soren/Projects/snake_ai/Graphics/body_vertical.png").convert_alpha()


MOVE_TO_IMAGE = {

    Direction.UP : {
        Direction.DOWN : body_vertical,
        Direction.LEFT : body_bottomleft,
        Direction.RIGHT: body_bottomright
    },

    Direction.RIGHT : {
        Direction.UP : body_topleft,
        Direction.DOWN : body_bottomleft,
        Direction.LEFT : body_horizontal
    },

    Direction.DOWN : {
        Direction.RIGHT : body_topright,
        Direction.DOWN : body_vertical,
        Direction.LEFT : body_topleft
    },

    Direction.LEFT : {
        Direction.UP : body_topright,
        Direction.DOWN : body_bottomright,
        Direction.LEFT : body_horizontal
    }
}