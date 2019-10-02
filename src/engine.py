import tcod as libtcod
import inputHandler
import renderer
import entities.actions as actions
import entities.fov as fov

from screen import Screen
from entities.entity import Entity
from entities.entity import create_entities
from mapping.map import Map



# First method. This is the python file that should be ran (on the cmd line).
def main():


    # Setting up screen information.
    screen = Screen(80, 45, "Python Roguelike", "../fonts/arial10x10.png")

    # Setting up font for the console.
    screen.setup_font()

    # Creating 2 consoles, the root console then the default console.
    screen.create_root_console()
    default_console = screen.create_console(screen.screen_width, screen.screen_height)

    # Setting up tile colors.
    # Using material design colors seen here:
    # https://htmlcolorcodes.com/color-chart/material-design-color-chart/
    tile_colors = {
        'dark_wall' : libtcod.Color(66,66,66),
        'dark_ground' : libtcod.Color(97,97,97),

        'light_wall' : libtcod.Color(117, 117, 117),
        'light_ground': libtcod.Color(238, 238, 238),

        'unseen' : libtcod.Color(33,33,33),
    }

    # Creating the map.
    map = Map(screen.screen_width, screen.screen_height, 5, 3, 20, 10, tile_colors)
    player_starting_pos = map.create_rooms()

    # Creating map for our FOV
    fov_map = fov.setup_fov(map)

    # Creating all of our entities.
    entityList = create_entities(default_console, player_starting_pos)

    # Setting player as the first entity in the list.
    # Player is always assumed to be the first entity in the entity list.
    player = entityList.get_list()[0]

    # Setting up keyboard and mouse inputs.
    key = libtcod.Key()
    mouse = libtcod.Mouse()

    # Setting initial FOV.
    fov.compute_fov(fov_map, player.x_position, player.y_position)

    # Renders the map using tile colors.
    # Will also render whenever a player moves (in the while loop).
    renderer.render_fov_map(default_console, map, fov_map)

    # While the window is open:
    while not libtcod.console_is_window_closed():

        # Gets the user input.
        action = inputHandler.handle_input(key, mouse)

        # Creating a new Action object.
        actions.Action(action, map, player, fov_map)

        # Performs console runtime functions (blitting, flushing, etc)
        renderer.console_runtime(default_console, entityList, screen, fov_map)


# Main function only gets ran if this file is called.
if __name__ == '__main__':
    main()
