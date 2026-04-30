# Class for the body parts
class Head:
    def __init__(self, position = (0, 0)) -> None:
        self.queue = list()
        self.pos = position

    def add_move(self, move: Direction)