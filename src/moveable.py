import libtcodpy as libtcod

# Class for movable objects in game.
class Moveable:

    # Constructor. Sets up the positioning and console the object appears on.
    def __init__(self, x_pos, y_pos, console):
        self.x_position = x_pos
        self.y_position = y_pos
        self.console = console

    # Setup new x and y positions for the object. This shouldn't be used externally.
    def  _move(self,new_x,new_y):
        self.x_position = new_x
        self.y_position = new_y

    # Returns x and y positions as a list.
    def getPos(self):
        return [self.x_position,self.y_position]

    # Update the position of a movable object.
    # new_positions should be a list = [x_coord,y_coord] where x and y are integers.
    def updatePosition(self, new_positions, character):

        # These positions are already stored in the object
        old_positions = self.getPos()

        # Replacing the old coordinates position with a blank
        # Otherwise the old character symbol wouldn't dissapear when the object moves.
        libtcod.console_put_char(self.console, old_positions[0], old_positions[1], ' ', libtcod.BKGND_NONE)

        # Setting up the new positions using _move.
        self._move(new_positions[0], new_positions[1])

        # Placing the object in the console at the new coordinates.
        self.placeEntity(character)

    # Place an entity in the world. Note that this doesn't overwrite it's last position.
    # Should normally only be used for first placing an object.
    def placeEntity(self, character):
        libtcod.console_put_char(self.console, self.x_position, self.y_position, character, libtcod.BKGND_NONE)
