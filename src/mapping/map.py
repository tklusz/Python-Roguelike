# Importing libtcod .
from mapping.tile import Tile

class Map:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.tiles = self.init_tiles()

    def init_tiles(self):
        tiles = [[Tile(False) for y in range(self.height)] for x in range(self.width)]

        tiles[30][22].blocking_movement = True
        tiles[30][22].blocking_sight = True
        tiles[31][22].blocking_movement = True
        tiles[31][22].blocking_sight = True
        tiles[32][22].blocking_movement = True
        tiles[32][22].blocking_sight = True

        return tiles

    def isBlockingMovement(self, x, y):
        return self.tiles[x][y].blocking_movement
