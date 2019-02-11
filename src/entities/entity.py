import tcod as libtcod
from entities.entityStorage import EntityStorage

# Class for entities.
class Entity:


    # Set the x position, y position, console the character should appear on,
    # representitive character ( e.g. @ ) and color.
    def __init__(self, x_pos, y_pos, console, char, color, player_flag = False):
        self.x_position = x_pos
        self.y_position = y_pos
        self.console = console
        self.character = char
        self.color = color
        self.is_player = player_flag


    # Setup new x and y positions for the object. This shouldn't be used externally.
    def  _move(self,new_x,new_y):
        self.x_position = new_x
        self.y_position = new_y

    # Returns x and y positions as a list.
    def get_position(self):
        return [self.x_position, self.y_position]

    # Replaces the entity character with a blank.
    # This can be used when moving or when an entity dies, or moves out of fov.
    def _replace_with_blank(self):

        # These positions are already stored in the object
        coordinates = self.get_position()

        # Replacing the coordinates position with a blank
        libtcod.console_put_char(self.console, coordinates[0], coordinates[1], ' ', libtcod.BKGND_NONE)

    # Update the position of an entity.
    # new_coordinates should be a list = [x_coord,y_coord] where x and y are integers.
    def update_position(self, new_coordinates, fov_map):

        # Otherwise the old character symbol wouldn't dissapear when the entity moves.
        self._replace_with_blank()

        # Setting up the new positions using _move.
        self._move(new_coordinates[0], new_coordinates[1])

        # Placing the object in the console at the new coordinates.
        self.place_entity(fov_map)

    # Place an entity in the world. Note that this doesn't overwrite it's last position.
    def place_entity(self, fov_map):

        # Will only place the entity if it's within FOV.
        if libtcod.map_is_in_fov(fov_map, self.x_position, self.y_position):

            # Setting the foreground to the entity's color.
            libtcod.console_set_default_foreground(self.console, self.color)

            # Putting the entity on the console at its specified positions.
            libtcod.console_put_char(self.console, self.x_position, self.y_position, self.character, libtcod.BKGND_NONE)

        # An entity outside of the FOV will be replaced with a blank.
        else:
            self._replace_with_blank()


# Creating entities
def create_entities(default_console, player_coordiantes):

    # Creating entity list
    entityList = []

    # Object has x-position, y-position, console, representitve character and color.
    # Player object should always be in the 0th index of the EntityStorage list.
    player = Entity(player_coordiantes[0], player_coordiantes[1], default_console, '@', libtcod.Color(33,33,33), True)
    npc = Entity(player_coordiantes[0]-1, player_coordiantes[1]-1, default_console, '@', libtcod.red)

    # Appending the player to the entity list.
    entityList.append(player)
    entityList.append(npc)

    # Creating and returning an EntityList object that stores all active entities.
    return EntityStorage(entityList)
