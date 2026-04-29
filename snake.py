import pygame
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720



class Snake:
    def __init__(self, board_size) -> None:
        self.board = [[0] * board_size for _ in range(board_size)]

    def run(self):
        """Main loop"""
        running = True
        while running:
            pass


def main():
    game = Snake(9)
    game.run()


if __name__ == "__main__":
    main()