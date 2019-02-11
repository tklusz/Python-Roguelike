import tcod as libtcod
import mapping.map as mapping

# Setting up our FOV map.
def setup_fov(base_map):

    # Creating a new libtcod map, the same size as our base map.
    fov_map = libtcod.map_new(base_map.width, base_map.height)

    # Looping through each tile of the map.
    for y in range(base_map.height):
        for x in range(base_map.width):

            # Setting each tile to not blocking sight or movement.
            libtcod.map_set_properties(fov_map, x, y,
                not base_map.tiles[x][y].blocking_sight,
                not base_map.tiles[x][y].blocking_movement)

    return fov_map

# Function to compute our FOV.
def compute_fov(fov_map, x, y, radius=6, light_walls=True, algorithm=0):
    fov_map.compute_fov(x, y, radius, light_walls, algorithm)
