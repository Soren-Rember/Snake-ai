import pygame
import time
from enum import Enum
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

class Direction(Enum):
    # Movement deltas
    UP = (-1, 0)
    DOWN = (+1, 0)
    LEFT = (0, -1)
    RIGHT = (0, +1)


class Snake:
    def __init__(self, board_size) -> None:
        self.board = [[0] * board_size for _ in range(board_size)]
        self.direction = Direction.UP
        self.position = 

    def parse_settings(self):
        with open("settings.txt", "r") as settings:
            lines = settings.readlines()
        self.board_size = int(lines[0])
        self.position = int(lines[1])

    def run(self):
        """Main loop"""
        running = True
        while running:
            time.sleep(0.75)
            print("fiouf")
            


def main():
    game = Snake(9)
    game.run()


if __name__ == "__main__":
    main()