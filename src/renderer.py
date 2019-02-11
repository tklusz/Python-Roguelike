import tcod as libtcod

import inputHandler
import engine

from entities.entity import Entity
from entities.entityStorage import EntityStorage
from mapping.map import Map


# Rendering map based on FOV.
def render_fov_map(console, map, fov_map):

    # Looping through each tile in our map.
    for x in range(map.width):
        for y in range(map.height):

            # This is deprecated. Switch to map_object.fov() in future.
            visible = libtcod.map_is_in_fov(fov_map, x, y)

            # If the tile at the current position is blocking sight, it's a wall.
            wall = map.tiles[x][y].blocking_sight

            # This is a tile currently in our FOV.
            if visible:
                # Wall in our FOV.
                if wall:
                     libtcod.console_set_char_background(console, x, y, map.tile_colors.get('light_wall'), libtcod.BKGND_SET)
                # Anything else in our FOV.
                else:
                    libtcod.console_set_char_background(console, x, y, map.tile_colors.get('light_ground'), libtcod.BKGND_SET)
                # Change the tile so that it has been seen by the player before.
                map.tiles[x][y].seen = True
            # If this is a tile we have seen before.
            elif map.tiles[x][y].seen:
                # Wall outside our FOV.
                if wall:
                    libtcod.console_set_char_background(console, x, y, map.tile_colors.get('dark_wall'), libtcod.BKGND_SET)
                # Anything else outside our FOV.
                else:
                    libtcod.console_set_char_background(console, x, y, map.tile_colors.get('dark_ground'), libtcod.BKGND_SET)
            # These are tiles that haven't been seen yet (normally black).
            else:
                libtcod.console_set_char_background(console, x, y, map.tile_colors.get('unseen'), libtcod.BKGND_SET)


# Function that modifies console during runtime.
def console_runtime(default_console, entity_list, screen, fov_map):

    # Placing each entity in our entity list.
    for entity in entity_list.get_list():
        entity.place_entity(fov_map)

    # Blitting the console
    screen.blit_to_root(default_console, 0, 0)

    # Redraw console
    libtcod.console_flush()
