from enum import Enum

class Direction(Enum):
    # Movement deltas
    UP = (-1, 0)
    DOWN = (+1, 0)
    LEFT = (0, -1)
    RIGHT = (0, +1)