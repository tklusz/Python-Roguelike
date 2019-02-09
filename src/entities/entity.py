import tcod as libtcod

# Class for entities.
class Entity:

    # Set the x position, y position, console the character should appear on,
    # representitive character ( e.g. @ ) and color.
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

    # Replaces the entity character with a blank.
    # This can be used when moving or when an entity dies.
    def _replace_with_blank(self):

        # These positions are already stored in the object
        coordinates = self.get_position()

        # Replacing the coordinates position with a blank
        libtcod.console_put_char(self.console, coordinates[0], coordinates[1], ' ', libtcod.BKGND_NONE)

    # Update the position of an entity.
    # new_coordinates should be a list = [x_coord,y_coord] where x and y are integers.
    def update_position(self, new_coordinates):

        # Otherwise the old character symbol wouldn't dissapear when the entity moves.
        self._replace_with_blank()

        # Setting up the new positions using _move.
        self._move(new_coordinates[0], new_coordinates[1])

        # Placing the object in the console at the new coordinates.
        self.place_entity()


    # Place an entity in the world. Note that this doesn't overwrite it's last position.
    def place_entity(self):

        # Setting the foreground to the entity's color.
        libtcod.console_set_default_foreground(self.console, self.color)

        # Putting the entity on the console at its specified positions.
        libtcod.console_put_char(self.console, self.x_position, self.y_position, self.character, libtcod.BKGND_NONE)
