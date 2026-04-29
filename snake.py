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
    def __init__(self) -> None:
        self.direction = Direction.UP

    def parse_settings(self):
        with open("settings.txt", "r") as settings:
            lines = settings.readlines()
        self.board_size = int(lines[0])

        y, x = lines[1].split(',')
        self.position = (int(y), int(x))

    def init_game(self):
        y, x = self.position

        self.board = [[0] * self.board_size for _ in range(self.board_size)]
        self.board[y][x] = 1

    def __str__(self):
        board_str = ''
        for y in range(self.board_size):
            for x in range(self.board_size):
                board_str += str(self.board[y][x])
            board_str += '\n'
        return board_str

    def run(self):
        """Main loop"""
        running = True
        while running:
            time.sleep(0.75)
            print(self)
            


def main():
    game = Snake()
    game.parse_settings()
    game.init_game()
    game.run()


if __name__ == "__main__":
    main()