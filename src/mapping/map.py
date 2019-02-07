# Importing our Tile class
from mapping.tile import Tile
from mapping.rectangle import Rectangle
from random import randint

# Class used to generate a map.
class Map:

    # Constructor
    def __init__(self, width, height, max_rooms, min_rooms, max_room_size, min_room_size, max_fails):
        self.width = width
        self.height = height

        self.max_rooms = max_rooms
        self.min_rooms = min_rooms

        self.max_room_size = max_room_size
        self.min_room_size = min_room_size

        self.max_fails = max_fails

        # Every time we generate a map object, we create a new set of tiles for the map.
        self.tiles = self.init_tiles()

    # Generating all of our tiles
    def init_tiles(self):

        # Generating a 2 dimentional array of tiles.
        # tiles[0][0] will be the top left corner, and so on.
        # Setting Tile(True) means that every tile is blocking movement and sight by default.
        tiles = [[Tile(True) for y in range(self.height)] for x in range(self.width)]

        return tiles

    # Actually generating the room tiles.
    def generate_room_tiles(self, room):

        # Looping through each tile in our rectangle and setting them to not block.
        # We are adding 1 as the walls for the room take up 1 tile, and remain blocking.
        for x in range(room.x_pos_top + 1, room.x_pos_bot):
            for y in range(room.y_pos_top + 1, room.y_pos_bot):
                # Changing this map's tiles to not blocking
                self.tiles[x][y].blocking_movement = False
                self.tiles[x][y].blocking_sight = False

    # Create rooms for the map. Also generates the player starting position.
    def create_rooms(self):

        rooms = []
        num_rooms = 0
        failed_attempts = 0

        rooms_to_create = randint(self.min_rooms, self.max_rooms)

        while num_rooms < rooms_to_create:

            if(failed_attempts == self.max_fails):
                self.create_room()

            rand_width = randint(self.min_room_size, self.max_room_size)
            rand_height = randint(self.min_room_size, self.max_room_size)

            rand_top_x = randint(0, self.width - rand_width - 1)
            rand_top_y = randint(0, self.height - rand_height - 1)

            rand_room = Rectangle(rand_top_x, rand_top_y, rand_width, rand_height)

            for other_room in rooms:
                 if rand_room.intersect(other_room):
                     failed_attempts+=1
                     break;
            else:
                self.generate_room_tiles(rand_room)
                [this_center_x, this_center_y] = rand_room.get_center()

                if num_rooms == 0:
                    player_starting_coords = [this_center_x, this_center_y]
                else:
                    [other_center_x, other_center_y] = rooms[num_rooms - 1].get_center()

                    if randint(0,1) == 1:
                        self.create_horziontal_tunnnel(other_center_x, this_center_x, other_center_y)
                        self.create_vertical_tunnel(other_center_y, this_center_y, this_center_x)
                    else:
                        self.create_vertical_tunnel(other_center_y, this_center_y, this_center_x)
                        self.create_horziontal_tunnnel(other_center_x, this_center_x, other_center_y)

                rooms.append(rand_room)
                num_rooms += 1

        return player_starting_coords


    # Used to create tunnels horizontally
    def create_horziontal_tunnnel(self, starting_x, ending_x, static_y):

        # We are changing as many tiles as the difference between starting and ending x positions.
        # Note that starting x could be to the right side of ending x (smaller number)
        # that is why we use a min() and max()
        # Example: createHoriziontalTunnels(10,5,3)
        # min(5,10) -> 5,
        # max(5,10) + 1 -> 11
        # Looping from 5 to 11. Drawing 7 tiles.
        # The y position is always the same, because we are staying on a horizontal line.
        for x_position in range( min(starting_x,ending_x) , max(starting_x, ending_x) + 1):
            self.tiles[x_position][static_y].blocking_movement = False
            self.tiles[x_position][static_y].blocking_sight = False

    # Used to create tunnels vertically.
    # Behaves almost the same as create_horizontal_tunnels, but the x is always the same.
    def create_vertical_tunnel(self, starting_y, ending_y, static_x):
        for y_position in range( min(starting_y,ending_y) , max(starting_y, ending_y) + 1):
            self.tiles[static_x][y_position].blocking_movement = False
            self.tiles[static_x][y_position].blocking_sight = False


    # Determine if our tile is blocking movement.
    def is_blocking_movement(self, x, y):
        return self.tiles[x][y].blocking_movement
