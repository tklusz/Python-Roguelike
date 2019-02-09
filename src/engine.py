# Importing libtcod and our other python files.
import tcod as libtcod
import inputHandler
import renderer
from screen import Screen
from entities.entity import Entity
from mapping.map import Map

# Main function that runs first.
def main():

    # Setting up screen information.
    screen = Screen(80, 45, "Python Roguelike", "../fonts/arial10x10.png")

    # Setting up font for the console
    screen.setup_font()

    # Creating 2 consoles, the root console then the default console.
    screen.create_root_console()
    default_console = screen.create_console(screen.screen_width, screen.screen_height)

    # Creating the map.
    map = Map(screen.screen_width, screen.screen_height, 5, 3, 20, 10)
    player_starting_pos = map.create_rooms()

    # Creating all of our entities
    entityList = renderer.create_entities(default_console, player_starting_pos)

    # Setting player as the first entity in the list.
    # Player is always assumed to be the first entity in the entity list.
    player = entityList.get_list()[0]

    # Setting up tile colors - will be moved to a class in future.
    tile_colors = {
        'dark_wall' : libtcod.Color(0,0,50),
        'dark_ground' : libtcod.Color(50,50,150)
    }

    # Setting up keyboard and mouse inputs.
    key = libtcod.Key()
    mouse = libtcod.Mouse()

    # While the window is open
    while not libtcod.console_is_window_closed():

        # Gets the user input.
        action = inputHandler.handle_input(key,mouse)

        # Renders the map using tile colors
        renderer.render_map(default_console, map, tile_colors)

        # Performs action based on user input.
        renderer.perform_actions(action, map, player)

        # Performs console runtime functions (blitting, flushing, etc)
        renderer.console_runtime(default_console, entityList, screen)


# Main function only gets ran if this file is called.
if __name__ == '__main__':
    main()
