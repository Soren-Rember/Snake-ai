import pygame

class Snake:
    def __init__(self, board_size) -> None:
        self.board = [[0] * board_size for _ in range(board_size)]

    def run(self):
        """Main loop"""
        running = True
        while running:
            for event in self.events:
                if event.type == pygame.QUIT:
                    running = False

    @property
    def events(self):
        return pygame.event.get()


def main():
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    clock = pygame.time.Clock()

    screen.fill("purple")

    # Render the game

    pygame.display.flip()

    clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()