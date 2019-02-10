import tcod as libtcod

import inputHandler
import engine

from entities.entity import Entity
from entities.entityStorage import EntityStorage
from mapping.map import Map


# Creating entities
def create_entities(default_console, player_position):

    # Creating entity list
    entityList = []

    # Object has x-position, y-position, console, representitve character and color.
    # Player object should always be in the 0th index of the EntityStorage list.
    player = Entity(player_position[0], player_position[1], default_console, '@', libtcod.white)

    # Appending the player to the entity list.
    entityList.append(player)

    # Creating and returning an EntityList object that stores all active entities.
    return EntityStorage(entityList)

# Performs an entity's actions based on the action event.
def perform_actions(action, map, entity):

    # Getting a move event from our eventhandler.
    move_event = action.get('move')

    # If the console recieved a move event.
    if (move_event):

        # Getting the new absolute x and y positions from the event.
        x_update = move_event[0]
        y_update = move_event[1]

        # Getting entity's positions.
        positions = entity.get_position()
        positions[0] += x_update
        positions[1] += y_update

        # Only allow the entity to move if the map isn't blocking movement.
        if not map.is_blocking_movement(positions[0], positions[1]):

            # Updating the new absolute position.
            entity.update_position(positions)

# Rendering the map using tile colors specified.
def render_map(console, map, tile_colors):

    # For each tile in the map:
    for y in range(map.height):
        for x in range(map.width):
            # Tile is a wall if it's blocking sight.
            wall = map.tiles[x][y].blocking_sight

            # Set walls to be the 'dark_wall' color specified in tile_colors.
            if wall:
                libtcod.console_set_char_background(console, x, y, tile_colors.get('dark_wall'), libtcod.BKGND_SET)
            # Set any other tile to be the 'dark_ground' color specified in
            # tile_colors.
            else:
                libtcod.console_set_char_background(console, x, y, tile_colors.get('dark_ground'), libtcod.BKGND_SET)

# Function that modifies console during runtime.
def console_runtime(default_console, entityList, screen):

    # Placing each entity in our entity list.
    for entity in entityList.get_list():
        entity.place_entity()

    # Blitting the console
    screen.blit_to_root(default_console, 0, 0)

    # Redraw console
    libtcod.console_flush()
