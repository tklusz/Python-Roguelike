# Importing libtcod and our other python files.
import tcod as libtcod
import inputHandler
import moveable

# Setting up global variables for screen info.
SCREEN_WIDTH = 80
SCREEN_HEIGHT = 50
FONT = '../fonts/arial10x10.png'
WINDOW_TITLE = "Libtcod RL"

# Main function that runs first.
def main():

    # Creating 2 consoles, the root console then the default console.
    consoles = consoleSetup()

    root_console = consoles[0]
    default_console = consoles[1]

    # Running function that sets up the player's starting position and '@' symbol.
    player = createPlayer(default_console)

    # Setting up keyboard and mouse inputs.
    key = libtcod.Key()
    mouse = libtcod.Mouse()

    # While the window is open
    while not libtcod.console_is_window_closed():

        # Gets the user input.
        action = inputHandler.handleInput(key,mouse)

        # Performs action based on user input.
        doPlayerActions(action, player)

        # Performs console runtime functions (blitting, flushing etc)
        consoleRuntime(default_console, root_console)



# Setting up the @ Player.
def createPlayer(default_console):

    # Getting default starting position based on window size.
    player_x = int(SCREEN_WIDTH/2)
    player_y = int(SCREEN_HEIGHT/2)

    # Creating player based on moveable object.
    # Object has x-position, y-position, console and representitve character.
    player = moveable.Moveable(player_x, player_y, default_console, '@')

    # Placing the player on the screen on the coordinates specified earlier.
    player.placeEntity()

    # Returns the player object after it has been created
    return player

# Function that creates the console_set_default_foreground window for the game.
def consoleSetup():

    # Setting our font, setting to greyscale, also setting the layout to TCOD
    libtcod.console_set_custom_font(FONT, libtcod.FONT_TYPE_GREYSCALE | libtcod.FONT_LAYOUT_TCOD)

    # Creating the root console.
    root_console = libtcod.console_init_root(SCREEN_WIDTH, SCREEN_HEIGHT, WINDOW_TITLE, False)

    # Creating a main console that gets overlayed on top of the root console.
    default_console = libtcod.console_new(SCREEN_WIDTH, SCREEN_HEIGHT)

    # Setting default console foreground color to white.
    libtcod.console_set_default_foreground(default_console, libtcod.white)


    return [root_console, default_console]

# Function that modifies console during runtime.
def consoleRuntime(default_console, root_console):

    # Blitting the console
    libtcod.console_blit(default_console, 0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, root_console, 0, 0)

    # Redraw console
    libtcod.console_flush()

# Gets the user's action
def doPlayerActions(action, moveable_object):

    move = action.get('move')

    if move:
        coordinates = moveable_object.getPos()
        dx, dy = move
        coordinates[0] += dx
        coordinates[1] += dy

        moveable_object.updatePosition(coordinates)



# Main function only gets ran if this file is called.
if __name__ == '__main__':
    main()
