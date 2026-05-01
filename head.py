from direction import Direction
import graphics_dict
import pygame

REVERSED_MOVE = {
    Direction.UP: Direction.DOWN,
    Direction.DOWN: Direction.UP,
    Direction.LEFT: Direction.RIGHT,
    Direction.RIGHT: Direction.LEFT
}

# Class for the body parts
class Body:
    def __init__(self, position = (0, 0), move = Direction.UP) -> None:
        self.pos = position
        self.dir = move
        self.image = pygame.image.load("Graphics/apple.png").convert_alpha()
        self.__rect = self.image.get_rect()
        

    @property
    def rect(self):
        self.__rect.centery = 20 + self.pos[0]*40
        self.__rect.centerx = 20 + self.pos[1]*40
        return self.__rect




class Head(Body):
    """
    We need this specifically for checking collisions and the validity of movements
    """
    def __init__(self, position=(0, 0), move=Direction.UP) -> None:
        super().__init__(position, move)


class Tail(Body):
    """
    We need a tail, with a short position history in order to spawn new body parts
    """
    def __init__(self, position=(0, 0), move=Direction.UP) -> None:
        super().__init__(position, move)
        self.last_position = ()

    def move(self):
        """Overwriting the move() method to include position and movement history"""