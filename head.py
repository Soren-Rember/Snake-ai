from direction import Direction
import pygame

# Class for the body parts
class Head:
    def __init__(self, position = (0, 0), move = Direction.UP) -> None:
        self.queue:list[Direction] = [move]
        self.pos = position
        self.image = pygame.transform.scale(pygame.image.load("Graphics/apple.png").convert_alpha(), (80, 80))
        self.__rect = self.image.get_rect()

    @property
    def rect(self):
        self.__rect.centery = 40 + self.pos[0]*80
        self.__rect.centerx = 40 + self.pos[1]*80
        return self.__rect

    def add_move(self, move: Direction):
        if self.queue:
            if move != self.queue[-1]:
                self.queue.append(move)
        else:
            self.queue.append(move)

    def move(self):
        if len(self.queue) > 1:
            move = self.queue.pop(0)
        else:
            move = self.queue[0]

        y, x = self.pos
        delta_y, delta_x = move.value

        y += delta_y
        x += delta_x

        self.pos = (y, x)


