import tcod as libtcod

# Screen, used to create various consoles.
class Screen:

    def __init__(self, screen_width, screen_height, window_title, font):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.title = window_title
        self.font = font

    def create_root_console(self):
        self.root_console = libtcod.console_init_root(self.screen_width, self.screen_height, self.title, False)

    # Creating a console.
    def create_console(self, width, height):
        return libtcod.console_new(width, height)

    # Setting our font, setting to greyscale, also setting the layout to TCOD
    def setup_font(self):
        return libtcod.console_set_custom_font(self.font, libtcod.FONT_TYPE_GREYSCALE | libtcod.FONT_LAYOUT_TCOD)

    # Blits console onto self's root console.
    def blit_to_root(self, new_console, x_pos, y_pos):
        libtcod.console_blit(new_console, x_pos, y_pos, self.screen_width, self.screen_height, self.root_console, 0, 0)
