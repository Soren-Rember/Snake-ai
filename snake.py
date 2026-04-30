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

# Class for the game
class Snake:
    def __init__(self) -> None:
        self.__state = dict()
        self.__dead = False
        self.__position = (0, 0)

    def parse_settings(self):
        with open("settings.txt", "r") as settings:
            lines = settings.readlines()
        self.board_size = int(lines[0])

        y, x = lines[1].split(',')
        self.position = (int(y), int(x))

    def init_game(self):
        self.__state = {
            "board": [[0] * self.board_size for _ in range(self.board_size)],
            "pos": self.position,
            "apple": None
        }
        

    def __str__(self):
        board_str = ''
        for y in range(self.board_size):
            for x in range(self.board_size):
                if (y, x) == self.position:
                    board_str += "1"
                else:
                    board_str += str(self.__state['board'][y][x])
            board_str += '\n'
        return board_str

    def run(self):
        """Main loop"""
        running = True
        while running:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_z]:
                self.move(Direction.UP)
            elif keys[pygame.K_s]:
                self.move(Direction.DOWN)
            elif keys[pygame.K_q]:
                self.move(Direction.LEFT)
            elif keys[pygame.K_d]:
                self.move(Direction.RIGHT)

            print(self)
            time.sleep(0.75)
            
    def move(self, dir: Direction):
        y, x = dir.value
        print("moving")
        self.position = (self.position[0] + y, self.position[1] + x)

# Class for the body parts
class Head:
    def __init__(self) -> None:
        self.queue = list()


def main():
    pygame.init()
    game = Snake()
    game.parse_settings()
    game.init_game()
    game.run()


if __name__ == "__main__":
    main()