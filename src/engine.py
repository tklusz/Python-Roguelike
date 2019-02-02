# Importing libtcod and our other python files.
import tcod as libtcod
import inputHandler
import renderer
from entity import Entity
from mapping.map import Map


# Setting up global variables for screen info.
SCREEN_WIDTH = 80
SCREEN_HEIGHT = 50
FONT = '../fonts/arial10x10.png'
WINDOW_TITLE = "Libtcod RL"

MAP_WIDTH = 80
MAP_HEIGHT = 45

# Main function that runs first.
def main():

    # Creating 2 consoles, the root console then the default console.
    consoles = consoleSetup()

    root_console = consoles[0]
    default_console = consoles[1]

    # Creating all of our entities
    renderer.createEntities(default_console)

    tile_colors = {
        'dark_wall' : libtcod.Color(0,0,100),
        'dark_ground' : libtcod.Color(50,50,150)
    }

    map = Map(MAP_WIDTH, MAP_HEIGHT)

    # Running function that sets up the player's starting position and '@' symbol.
    player = renderer.ENTITIES[0]

    # Setting up keyboard and mouse inputs.
    key = libtcod.Key()
    mouse = libtcod.Mouse()

    # While the window is open
    while not libtcod.console_is_window_closed():

        # Gets the user input.
        action = inputHandler.handleInput(key,mouse)

        renderer.renderMap(default_console, map, tile_colors)

        # Performs action based on user input.
        renderer.performActions(action, map, player)

        # Performs console runtime functions (blitting, flushing etc)
        renderer.consoleRuntime(default_console, root_console)


# Function that creates the console_set_default_foreground window for the game.
def consoleSetup():

    # Setting our font, setting to greyscale, also setting the layout to TCOD
    libtcod.console_set_custom_font(FONT, libtcod.FONT_TYPE_GREYSCALE | libtcod.FONT_LAYOUT_TCOD)

    # Creating the root console.
    root_console = libtcod.console_init_root(SCREEN_WIDTH, SCREEN_HEIGHT, WINDOW_TITLE, False)

    # Creating a main console that gets overlayed on top of the root console.
    default_console = libtcod.console_new(SCREEN_WIDTH, SCREEN_HEIGHT)


    return [root_console, default_console]

# Main function only gets ran if this file is called.
if __name__ == '__main__':
    main()
