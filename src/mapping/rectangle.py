# Class used for generating a rectangle.
# This is used for carving out rooms in the map generator.
class Rectangle:


    # Rectangle(1,2,2,3)
    #
    #     (x_pos_top, y_pos_top) - Starting coordinate.
    #     (1,2)  #   #   #   #
    #       #                #
    #       #   #    #   #  (3,5)
    #                       (x_pos_bot,y_pos_bot) - Ending coordinate.

    def __init__(self, x_coordinate, y_coordinate, width, height):
        self.x_pos_top = x_coordinate
        self.y_pos_top = y_coordinate

        self.x_pos_bot = x_coordinate + width
        self.y_pos_bot = y_coordinate + height

    # Returns the center position of the rectangle.
    # Note that this might not be the direct center if the sides are odd.
    def get_center(self):

        #  a = (1,1). b = (7,5)
        #
        #   a######   center_x_coord = a.x_position + b.x_position / 2
        #   #     #                        (1)      +    (7)       / 2 = 4
        #   #  o  #   center_y_coord = a.y_position + b.y_position / 2
        #   #     #                        (1)      +    (5)       / 2 = 3
        #   ######b   o = (center_x_coord, center_y_coord)
        #

        center_x_coord = int((self.x_pos_top + self.x_pos_bot) / 2)
        center_y_coord = int((self.y_pos_top + self.y_pos_bot) / 2)

        return [center_x_coord, center_y_coord]

    # Determines if this rectangle intersects with another rectangle
    def intersect(self, other_rectangle):

        # We require all 4 of these conditions to be true for an overlap.
        # Left as separate if statements to increase readability.
        if self.x_pos_top <= other_rectangle.x_pos_bot:
            if self.x_pos_bot >= other_rectangle.x_pos_top:
                if self.y_pos_top <= other_rectangle.y_pos_bot:
                    if self.y_pos_bot >= other_rectangle.y_pos_top:
                        return True
        return False
