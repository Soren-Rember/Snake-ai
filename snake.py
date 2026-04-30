import pygame
import time

from direction import Direction
from head import Head
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800

# Class for the game
class Snake:
    def __init__(self) -> None:
        self.__state = dict()
        self.__snake: list[Head] = []

        #Pygame init
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()

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

    def draw_background(self):
        width = SCREEN_WIDTH//self.board_size
        height = SCREEN_HEIGHT//self.board_size
        checker_pattern = 0
        for y in range(self.board_size):
            for x in range(self.board_size):
                square = pygame.Rect()
                square.topleft = (x*width, y*height)
                square.height = height
                square.width = width
                if x % 2 == checker_pattern % 2:
                    color = "chartreuse3"
                else:
                    color = "chartreuse2"
                pygame.draw.rect(self.screen, color, square)
            checker_pattern += 1
            

    def run(self):
        """Main loop"""
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.screen.fill('black')
            self.draw_background()

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

            pygame.display.flip()

            self.step()

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