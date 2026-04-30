import pygame
import time

from direction import Direction
from head import Head
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

# Class for the game
class Snake:
    def __init__(self) -> None:
        self.__state = dict()

    def parse_settings(self):
        with open("settings.txt", "r") as settings:
            lines = settings.readlines()
        self.board_size = int(lines[0])
        y, x = lines[1].split(',')

        self.__state = {
            "board": [[0] * self.board_size for _ in range(self.board_size)],
            "snake": [Head((int(y), int(x)))],
            "apple": None
        }

    @property
    def head(self):
        return self.__state['snake'][0]

    def __str__(self):
        board_str = ''
        for y in range(self.board_size):
            for x in range(self.board_size):
                if (y, x) == self.head.pos:
                    board_str += "1"
                elif (y, x) == self.__state['apple']:
                    board_str += "2"
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


def main():
    pygame.init()
    game = Snake()
    game.parse_settings()
    game.init_game()
    game.run()


if __name__ == "__main__":
    main()