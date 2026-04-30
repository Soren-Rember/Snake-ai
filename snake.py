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
        self.__snake: list[Head] = []

    def parse_settings(self):
        with open("settings.txt", "r") as settings:
            lines = settings.readlines()
        self.board_size = int(lines[0])
        y, x = lines[1].split(',')

        self.__snake = [Head((int(y), int(x)))]
        self.__board = [[0] * self.board_size for _ in range(self.board_size)]
        self.__apple = None

    @property
    def head(self):
        return self.__snake[0]

    def __str__(self):
        board_str = ''
        for y in range(self.board_size):
            for x in range(self.board_size):
                if (y, x) == self.head.pos:
                    board_str += "1"
                elif (y, x) == self.__apple:
                    board_str += "2"
                else:
                    board_str += "0"
            board_str += '\n'
        return board_str

    def run(self):
        """Main loop"""
        running = True
        while running:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_z]:
                print("detected key z")
                self.new_move(Direction.UP)
            elif keys[pygame.K_s]:
                self.new_move(Direction.DOWN)
            elif keys[pygame.K_q]:
                self.new_move(Direction.LEFT)
            elif keys[pygame.K_d]:
                self.new_move(Direction.RIGHT)

            self.step()

            print(self)

            time.sleep(0.75)
            
    def new_move(self, move: Direction):
        for head in self.__snake:
            head.add_move(move)
    
    def step(self):
        #move every head
        for head in self.__snake:
            head.move()


def main():
    pygame.init()
    game = Snake()
    game.parse_settings()
    game.run()


if __name__ == "__main__":
    main()