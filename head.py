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
        self.queue:list[Direction] = [move]
        self.pos = position
        self.image = pygame.image.load("Graphics/apple.png").convert_alpha()
        self.__rect = self.image.get_rect()
        self.last_state = (self.pos, move)

    @property
    def rect(self):
        self.__rect.centery = 20 + self.pos[0]*40
        self.__rect.centerx = 20 + self.pos[1]*40
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

        if move == REVERSED_MOVE[self.last_state[1]]:
            return
        
        y, x = self.pos
        delta_y, delta_x = move.value

        y += delta_y
        x += delta_x

        self.pos = (y, x)


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