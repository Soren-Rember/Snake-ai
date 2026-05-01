import pygame
import random

from images import HEAD_IMAGES, TAIL_IMAGES, BODY_IMAGES

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 400

BOARD_SIZE = 10

INT_ID_TO_MOVE = {
    1073741906: "UP",
    1073741905: "DOWN",
    1073741904: "LEFT",
    1073741903: "RIGHT"
}

MOVE_DELTAS = {
    "UP" : (-1, 0),
    "DOWN": (1, 0),
    "LEFT": (0, -1),
    "RIGHT": (0, 1)
}

DELTA_MOVES = {
    (-1, 0): "UP",
    (1, 0): "DOWN",
    (0, -1): "LEFT",
    (0, 1): "RIGHT" 
}

REVERSED_MOVE = {
    "UP": "DOWN",
    "DOWN": "UP",
    "LEFT": "RIGHT",
    "RIGHT": "LEFT"
}

# Class for the game
class Snake:
    def __init__(self) -> None:
        self.__state = dict()
        self.__snake: list[tuple[int, int]] = [(5, 5), (4, 5)]
        self.__move = "UP"

        #Pygame init
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()


    def draw_background(self):
        width = SCREEN_WIDTH//BOARD_SIZE
        height = SCREEN_HEIGHT//BOARD_SIZE
        checker_pattern = 0
        for y in range(BOARD_SIZE):
            for x in range(BOARD_SIZE):
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
        GROW_EVENT = pygame.USEREVENT + 2
        MOVE_EVENT = pygame.USEREVENT + 1
        pygame.time.set_timer(MOVE_EVENT, 500)
        pygame.time.set_timer(GROW_EVENT, 2000)
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == MOVE_EVENT:
                    self.step()
                elif event.type == pygame.KEYDOWN:
                    if event.key in INT_ID_TO_MOVE:
                        self.__move = INT_ID_TO_MOVE[event.key]
                elif event.type == GROW_EVENT:
                    self.step(grow=True)



            self.screen.fill('black')
            self.draw_background()
            self.draw_snake()

            pygame.display.flip()

            self.clock.tick(60)
        

    def step(self, grow = False):
        delta_y, delta_x = MOVE_DELTAS[self.__move]
        y, x = self.__snake[0]
        y += delta_y
        x += delta_x
        self.__snake.insert(0, (y, x))
        if not grow:
            self.__snake.pop()

    
    def draw_snake(self):
        for i in range(len(self.__snake)):
            if i == 0:
                part = self.get_image(None, self.__snake[0], self.__snake[1])
                part_rect = pygame.Surface.get_rect(part)
                part_rect.centery = 20 + 40* self.__snake[0][0]
                part_rect.centerx = 20 + 40* self.__snake[0][1]

            elif i == len(self.__snake) -1:
                part = self.get_image(self.__snake[-2], self.__snake[-1], None)
                part_rect = pygame.Surface.get_rect(part)
                part_rect.centery = 20 + 40* self.__snake[-1][0]
                part_rect.centerx = 20 + 40* self.__snake[-1][1]

            else:
                part = self.get_image(self.__snake[i-1], self.__snake[i], self.__snake[i+1])
                part_rect = pygame.Surface.get_rect(part)
                part_rect.centery = 20 + 40* self.__snake[i][0]
                part_rect.centerx = 20 + 40* self.__snake[i][1]


            self.screen.blit(part, part_rect)


    def get_image(self, previous:tuple, actual:tuple, next:tuple):
        y, x = actual
        
        # HEAD
        if previous is None:
            y -= next[0]
            x -= next[1]
            return HEAD_IMAGES[DELTA_MOVES[(y, x)]]
        
        # TAIL
        elif next is None:
            y -= previous[0]
            x -= previous[1]
            return TAIL_IMAGES[DELTA_MOVES[(y, x)]]
        
        else:
            y = previous[0] - actual[0]
            x = previous[1] - actual[1]
            previous_move = (y, x)
            y = actual[0] - next[0]
            x = actual[1] - next[1]
            next_move = (y, x)
            return BODY_IMAGES[DELTA_MOVES[next_move]][DELTA_MOVES[previous_move]]

            

def main(): 
    pygame.init()
    game = Snake()
    game.run()


if __name__ == "__main__":
    main()