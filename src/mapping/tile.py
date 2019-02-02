
class Tile:
    def __init__(self, blocking_movement, blocking_sight=True):
        self.blocking_movement = blocking_movement

        if blocking_sight:
            blocking_sight = blocking_movement

        self.blocking_sight = blocking_sight
