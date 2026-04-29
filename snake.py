import pygame

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

screen.fill("purple")

# Render the game

pygame.display.flip()

clock.tick(60)

pygame.quit()

class Snake:
    def __init__(self, board_size) -> None:
        self.board = [[0] * board_size for _ in range(board_size)]

        