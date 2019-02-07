import tcod as libtcod

# Class for movable objects in game.
class Entity:

    # Constructor. Sets up the positioning and console the object appears on.
    def __init__(self, x_pos, y_pos, console, char, color):
        self.x_position = x_pos
        self.y_position = y_pos
        self.console = console
        self.character = char
        self.color = color

    # Setup new x and y positions for the object. This shouldn't be used externally.
    def  _move(self,new_x,new_y):
        self.x_position = new_x
        self.y_position = new_y

    # Returns x and y positions as a list.
    def get_position(self):
        return [self.x_position, self.y_position]

    # Update the position of a movable object.
    # new_positions should be a list = [x_coord,y_coord] where x and y are integers.
    def update_position(self, new_coordinates):

        # Otherwise the old character symbol wouldn't dissapear when the entity moves.
        self._replace_with_blank()

        # Setting up the new positions using _move.
        self._move(new_coordinates[0], new_coordinates[1])

        # Placing the object in the console at the new coordinates.
        self.place_entity()

    # Replaces the entity character with a blank.
    # This can be used when moving or when an entity dies.
    def _replace_with_blank(self):

        # These positions are already stored in the object
        coordinates = self.get_position()

        # Replacing the coordinates position with a blank
        libtcod.console_put_char(self.console, coordinates[0], coordinates[1], ' ', libtcod.BKGND_NONE)


    # Place an entity in the world. Note that this doesn't overwrite it's last position.
    # Should normally only be used for first placing an object.
    def place_entity(self):

        libtcod.console_set_default_foreground(self.console, self.color)
        libtcod.console_put_char(self.console, self.x_position, self.y_position, self.character, libtcod.BKGND_NONE)
