# Importing required classes.
from mapping.tile import Tile
from mapping.rectangle import Rectangle
from random import randint

# Class used to generate a map.
class Map:


    # Constructor
    def __init__(self, width, height, max_rooms, min_rooms, max_room_size,
                 min_room_size, tile_colors):
        """
        Parameters
        ----------
        width: int.
            Width the map should be when generated (a # of tiles).
        height: int.
            Height the map should be when generated (a # of tiles).
        max_rooms: int.
            Maximum number of rooms to generate when making the map.
        min_rooms: int.
            Minimum number of rooms to generate when making the map.
            The actual number of rooms will be a random number
            between the maximum and minimum.
        max_room_size: int.
            Maximum number of tiles a room takes up
            (horizontally or vertically).
        min_room_size: int.
            Minimum number of tiles a room takes up
            (horizontally or vertically).
            The actual number of rooms will be a random between min and max.
        tile_colors: dictionary.
            Dictionary of tile types and their associated color.
        """

        self.width = width
        self.height = height

        self.max_rooms = max_rooms
        self.min_rooms = min_rooms

        self.max_room_size = max_room_size
        self.min_room_size = min_room_size

        self.tile_colors = tile_colors

        # Every time we generate a map object, we will also generate the tiles
        # for the map.
        self.tiles = self.init_tiles()

    # Creating and returning a 2d array representing the map.
    def init_tiles(self):

        # Output:
        # 10x50 map example. B = Blocking sight and movement.
        #
        # BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB
        # BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB
        # BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB
        # BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB
        # BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB
        # BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB
        # BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB
        # BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB
        # BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB
        # BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB
        #

        # Generating a 2 dimentional array of tiles.
        # tiles[0][0] will be the top left corner, and so on.
        # Setting Tile(True) means that every tile is blocking movement
        # and sight by default.
        tiles = [[Tile(True) for y in range(self.height)]
                for x in range(self.width)]

        # The 2d array that is returned will be the same size as the map,
        # each position will be = a tile object.
        return tiles

    # Clears out a section of the map for a room.
    def generate_room_tiles(self, room):

        # Output:
        # 10x50 map example. With 1 5x5 room
        # B = Blocking sight and movement.
        # Blank = able to be moved and seen through.
        #
        # BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB
        # BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB
        # BBBBBBBB     BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB
        # BBBBBBBB     BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB
        # BBBBBBBB     BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB
        # BBBBBBBB     BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB
        # BBBBBBBB     BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB
        # BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB
        # BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB
        # BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB
        #

        # Looping through every tile in our room.
        for x in range(room.x_pos_top + 1, room.x_pos_bot):
            for y in range(room.y_pos_top + 1, room.y_pos_bot):

                # Changing this map's tiles to not blocking at each tile in
                # the room.
                self.tiles[x][y].blocking_movement = False
                self.tiles[x][y].blocking_sight = False

    # Create rooms for the map. Also generates and returns the
    # player's starting position.
    def create_rooms(self):

        # List of currently generated rooms.
        rooms = []

        # Number of rooms generated so far.
        num_rooms = 0

        # Number of rooms for the method to create.
        rooms_to_create = randint(self.min_rooms, self.max_rooms)

        # Looping until we have the required amount of rooms.
        while num_rooms < rooms_to_create:

            # Generating 1 random room.
            rand_room = self.generate_single_room()

            # Looping through all rooms we already created.
            for other_room in rooms:
                 # If our new room intersects any of those rooms, retry.
                 if rand_room.intersect(other_room):
                     break;

            # If we generate a successful room:
            else:

                # Change the map tiles to make the room moveable.
                self.generate_room_tiles(rand_room)

                # Getting coordinates of the center of this room.
                [this_center_x, this_center_y] = rand_room.get_center()

                # If this is the first room, put our player in the center position.
                if num_rooms == 0:
                    player_starting_coords = [this_center_x, this_center_y]

                # If this isn't the first room.
                else:

                    # Getting the previous room's center position.
                    [prev_center_x, prev_center_y] = rooms[num_rooms - 1].get_center()

                    # Generate tunnels that connect this room to our previous room:
                    self.attach_room(this_center_x, this_center_y, prev_center_x, prev_center_y)

                # Adding this room to the list of rooms, adding 1 to num_rooms.
                rooms.append(rand_room)
                num_rooms += 1

        # Returning player's coordinates that will be used to place the player.
        return player_starting_coords


    # Generates a single room based on the Map object's attributes.
    def generate_single_room(self):

        # Generating a random width and height for the room
        rand_width = randint(self.min_room_size, self.max_room_size)
        rand_height = randint(self.min_room_size, self.max_room_size)

        # Setting the top left coordinate for the rectangle
        # that represents the room.
        rand_top_x = randint(0, self.width - rand_width - 1)
        rand_top_y = randint(0, self.height - rand_height - 1)

        # Creating the rectangle that represents the room.
        # Rectangle will start at (rand_top_x, rand_top_y).
        # And continue horizontally a number of tiles = rand_height.
        # Will also continue vertically a number of tiles = rand_width.
        return Rectangle(rand_top_x, rand_top_y, rand_width, rand_height)

    # Attaching a room to previous room.
    def attach_room(self, this_center_x, this_center_y, prev_center_x, prev_center_y):

        # 50/50 chance to generate vertical or horizontal tunnel first.
        if randint(0,1) == 1:

            # Creating a tunnel from this room to the previous room.
            self.create_horziontal_tunnnel(prev_center_x, this_center_x, prev_center_y)
            self.create_vertical_tunnel(prev_center_y, this_center_y, this_center_x)
        else:
            self.create_vertical_tunnel(prev_center_y, this_center_y, this_center_x)
            self.create_horziontal_tunnnel(prev_center_x, this_center_x, prev_center_y)


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
        for x_position in range(min(starting_x,ending_x) , max(starting_x, ending_x) + 1):
            self.tiles[x_position][static_y].blocking_movement = False
            self.tiles[x_position][static_y].blocking_sight = False

    # Used to create tunnels vertically.
    # Behaves almost the same as create_horizontal_tunnels, but the x is always the same.
    def create_vertical_tunnel(self, starting_y, ending_y, static_x):
        for y_position in range(min(starting_y,ending_y) , max(starting_y, ending_y) + 1):
            self.tiles[static_x][y_position].blocking_movement = False
            self.tiles[static_x][y_position].blocking_sight = False


    # Determine if our tile is blocking movement.
    def is_blocking_movement(self, x, y):
        return self.tiles[x][y].blocking_movement
