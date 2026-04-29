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
        self.dead = False

    @property
    def position(self):
        return self.position
    
    @position.setter
    def position(self, pos:tuple[int, int]):
        y, x = pos
        if y > 0 and y < self.board_size:
            if x > 0 and x < self.board_size:
                self.position = (y, x)
        else:
            self.dead = True

    def parse_settings(self):
        with open("settings.txt", "r") as settings:
            lines = settings.readlines()
        self.board_size = int(lines[0])

        y, x = lines[1].split(',')
        self.position = (int(y), int(x))

    def init_game(self):
        y, x = self.position

        self.board = [[0] * self.board_size for _ in range(self.board_size)]
        self.state = {"board" : self.board, "pos" : self.position}
        

    def __str__(self):
        board_str = ''
        for y in range(self.board_size):
            for x in range(self.board_size):
                if (y, x) == self.position:
                    board_str += "1"
                else:
                    board_str += str(self.board[y][x])
            board_str += '\n'
        return board_str

    def run(self):
        """Main loop"""
        running = True
        while running:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_UP]:
                self.position = (self.position[0] + self.direction.value[0], self.position[1] + self.direction.value[1])
            print(self)
            time.sleep(0.75)
            


def main():
    pygame.init()
    game = Snake()
    game.parse_settings()
    game.init_game()
    game.run()


if __name__ == "__main__":
    main()