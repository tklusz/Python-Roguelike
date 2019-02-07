# Importing libtcod and our other python files.
import tcod as libtcod
import inputHandler
from entities.entity import Entity
from entities.entityStorage import EntityStorage
from mapping.map import Map
import engine

# Creating entities
def create_entities(default_console, player_position):

    # Creating entity list
    entityList = []

    # Object has x-position, y-position, console, representitve character and color.
    # Player object should always be in the 0th index of the EntityStorage list.
    player = Entity(player_position[0], player_position[1], default_console, '@', libtcod.white)


    entityList.append(player)

    # Creating and returning an entity list that stores all active entities.
    return EntityStorage(entityList)

# Performs an entitie's actions based on the action event.
def perform_actions(action, map, entity):

    move_event = action.get('move')

    # If the console recieved a move event.
    if (move_event):

        # Getting the new absolute x and y positions from the event.
        x_update = move_event[0]
        y_update = move_event[1]

        positions = entity.get_position()
        positions[0] += x_update
        positions[1] += y_update

        # Only allow the entity to move if the map isn't blocking movement.
        if not map.is_blocking_movement(positions[0], positions[1]):

            # Updating the new absolute position.
            entity.update_position(positions)

def render_map(console, map, tile_colors):
    for y in range(map.height):
        for x in range(map.width):
            wall = map.tiles[x][y].blocking_sight

            if wall:
                libtcod.console_set_char_background(console, x, y, tile_colors.get('dark_wall'), libtcod.BKGND_SET)
            else:
                libtcod.console_set_char_background(console, x, y, tile_colors.get('dark_ground'), libtcod.BKGND_SET)



# Function that modifies console during runtime.
def console_runtime(default_console, entityList, screen):

    for entity in entityList.get_list():
        entity.place_entity()

    # Blitting the console
    screen.blit_to_root(default_console, 0, 0)

    # Redraw console
    libtcod.console_flush()
