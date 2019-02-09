# Class for tiles used in maps.
class Tile:

    # Set if the tile is blocking movement or sight.
    def __init__(self, blocking_movement, blocking_sight=True):
        self.blocking_movement = blocking_movement

        # If the tile is blocking sight, it automatically blocks movement.
        if blocking_sight:
            blocking_sight = blocking_movement

        self.blocking_sight = blocking_sight
