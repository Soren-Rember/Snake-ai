import pygame
import random

from images import *

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
        self.__snake: list[tuple[int, int]] = [(4, 5), (5, 5)]
        self.__apple: tuple[int, int] = (0, 0)
        self.__move = "UP"


        self.apple_image = pygame.image.load("Graphics/apple.png").convert_alpha()
        self.apple_rect = pygame.Surface.get_rect(self.apple_image)

        #Pygame init
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.dead = False


    def draw_background(self):
        self.screen.blit(BACKGROUND_IMAGE, BACKGROUND_RECT)

    def run(self):
        """Main loop"""
        running = True
        MOVE_EVENT = pygame.USEREVENT + 1
        pygame.time.set_timer(MOVE_EVENT, 500)
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == MOVE_EVENT:
                    self.step()
                elif event.type == pygame.KEYDOWN:
                    if event.key in INT_ID_TO_MOVE:
                        move = INT_ID_TO_MOVE[event.key]
                        if move != REVERSED_MOVE[self.__move]:
                            self.__move = INT_ID_TO_MOVE[event.key]



            self.screen.fill('black')
            self.draw_background()
            if self.dead:
                input()
            self.draw_snake()
            self.draw_apple()

            pygame.display.flip()

            self.clock.tick(60)
        

    def step(self):
        delta_y, delta_x = MOVE_DELTAS[self.__move]
        y, x = self.__snake[0]
        y += delta_y
        x += delta_x
        if ((y, x) in self.__snake[1:]) or (y < 0 or y>= BOARD_SIZE) or (x < 0 or x>= BOARD_SIZE):
            print("yep", (y, x) in self.__snake[1:], self.__snake[1:])
            self.dead = True
        self.__snake.insert(0, (y, x))

        if (y, x) != self.__apple:
            self.__snake.pop()
        else:
            self.spawn_apple()

    def spawn_apple(self):
        choice = (random.randint(0, 9), random.randint(0, 9))
        while choice in self.__snake:
            choice = (random.randint(0, 9), random.randint(0, 9))
        self.__apple = choice 


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

    def draw_apple(self):
        self.apple_rect.centery = 20 + 40*self.__apple[0]
        self.apple_rect.centerx = 20 + 40*self.__apple[1]
        self.screen.blit(self.apple_image, self.apple_rect)

    def get_image(self, previous:tuple|None, actual:tuple, next:tuple|None):
        y, x = actual
        
        # HEAD
        if previous is None:
            assert next is not None
            y -= next[0]
            x -= next[1]
            return HEAD_IMAGES[DELTA_MOVES[(y, x)]]
        
        # TAIL
        elif next is None:
            assert previous is not None
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