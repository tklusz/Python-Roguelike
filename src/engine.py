# Importing libtcod and our other python files.
import libtcodpy as libtcod
import inputHandler
import moveable

# Setting up global variables for screen info.
SCREEN_WIDTH = 80
SCREEN_HEIGHT = 50
FONT = '../fonts/arial10x10.png'
WINDOW_TITLE = "Libtcod RL"

# Main function that runs first.
def main():

    # Actually creating the screen. We use the global variables we set up earlier.
    default_console = createScreen(FONT, WINDOW_TITLE)

    # Running function that sets up the player's starting position and '@' symbol.
    player = setupPlayer(default_console)

    # Setting up keyboard and mouse inputs.
    key = libtcod.Key()
    mouse = libtcod.Mouse()

    # While the window is open
    while not libtcod.console_is_window_closed():

        # Gets the user input.
        action = inputHandler.handleInput(key,mouse)

        # Handles console updates during runtime.
        consoleRuntime(default_console)

        # Handles the action from user input.
        handleActions(action, player)


# Console functions done during the game loop.
def consoleRuntime(console):

    # Setting default console foreground color to white.
    libtcod.console_set_default_foreground(console, libtcod.white)

    # Blitting the console
    libtcod.console_blit(console, 0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, 0, 0, 0)

    # Redraw console
    libtcod.console_flush()


# Function that creates the console window for the game.
def createScreen(font, title):

    # Setting our font, setting to greyscale, also setting the layout to TCOD
    libtcod.console_set_custom_font(font, libtcod.FONT_TYPE_GREYSCALE | libtcod.FONT_LAYOUT_TCOD)

    # Creating the console window.
    libtcod.console_init_root(SCREEN_WIDTH, SCREEN_HEIGHT, title, False)

    # Returns the console.
    console = libtcod.console_new(SCREEN_WIDTH, SCREEN_HEIGHT)

    return console

# Handles user Actions
def handleActions(action, moveable_object):

    move = action.get('move')

    if move:
        coordinates = moveable_object.getPos()
        dx, dy = move
        coordinates[0] += dx
        coordinates[1] += dy

        moveable_object.updatePosition(coordinates, '@')


# Setting up the @ Player.
def setupPlayer(default_console):

    # Getting default starting position based on window size.
    player_x = int(SCREEN_WIDTH/2)
    player_y = int(SCREEN_HEIGHT/2)

    # Creating player object
    player = moveable.Moveable(player_x, player_y, default_console)

    # Placing the player on the screen on the coordinates specified earlier.
    player.placeEntity('@')

    # Returns the player object after it has been created
    return player

# Main function only gets ran if this file is called.
if __name__ == '__main__':
    main()
