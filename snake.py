import pygame
import time

from direction import Direction
from head import Head
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 400

INT_ID_TO_MOVE = {
    1073741906: Direction.UP,
    1073741905: Direction.DOWN,
    1073741904: Direction.LEFT,
    1073741903: Direction.RIGHT
}

# Class for the game
class Snake:
    def __init__(self) -> None:
        self.__state = dict()
        self.__snake: list[Head] = []
        self.__move = Direction.UP

        #Pygame init
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()

    def parse_settings(self):
        with open("settings.txt", "r") as settings:
            lines = settings.readlines()
        self.board_size = int(lines[0])
        y, x = lines[1].split(',')

        self.__snake = [Head((5,5)), Head((4,5))]
        self.__apple = None

    @property
    def head(self):
        return self.__snake[0]
    
    @property
    def tail(self):
        return self.__snake[-1]

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
        ELONGATE_EVENT = pygame.USEREVENT + 2
        MOVE_EVENT = pygame.USEREVENT + 1
        pygame.time.set_timer(MOVE_EVENT, 500)
        pygame.time.set_timer(ELONGATE_EVENT, 2000)
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == MOVE_EVENT:
                    self.step()
                elif event.type == pygame.KEYDOWN:
                    if event.key in INT_ID_TO_MOVE:
                        self.__move = INT_ID_TO_MOVE[event.key]
                elif event.type == ELONGATE_EVENT:
                    self.step(False)


            self.screen.fill('black')
            self.draw_background()
            self.draw()

            pygame.display.flip()

            self.clock.tick(60)
            
    
    def draw(self):
        for head in self.__snake:
            position = head.rect
            self.screen.blit(head.image, position)

    def step(self, pop = True):
        #move every head
        y, x = self.__snake[0].pos
        delta_y, delta_x = self.__snake[0].dir.value
        y += delta_y
        x += delta_x
        self.__snake.insert(0, Head(position=(y, x), move=self.__move))
        if pop:
            self.__snake.pop()

def main():
    pygame.init()
    game = Snake()
    game.parse_settings()
    game.run()


if __name__ == "__main__":
    main()