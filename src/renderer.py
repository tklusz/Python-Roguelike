# Importing libtcod and our other python files.
import tcod as libtcod
import inputHandler
from entity import Entity
from mapping.map import Map
import engine


ENTITIES = []

# Creating entities
def createEntities(default_console):

    # Object has x-position, y-position, console, representitve character and color.
    npc = Entity(int(engine.SCREEN_WIDTH/2)-4, int(engine.SCREEN_HEIGHT/2), default_console, '@', libtcod.red)
    # Object has x-position, y-position, console, representitve character and color.
    player = Entity(int(engine.SCREEN_WIDTH/2), int(engine.SCREEN_HEIGHT/2), default_console, '@', libtcod.white)

    ENTITIES.append(player)
    ENTITIES.append(npc)

# Gets the user's action
def performActions(action, map, entity):

    move_event = action.get('move')

    # If the console recieved a move event.
    if (move_event):

        # Getting the new relative x and y positions from the event.
        x_update = move_event[0]
        y_update = move_event[1]

        positions = entity.getPos()
        positions[0] += x_update
        positions[1] += y_update

        if not map.isBlockingMovement(positions[0], positions[1]):
            # Updating the new relative position.
            print(positions)
            entity.updatePosition(positions)

def renderMap(console, map, tile_colors):
    for y in range(map.height):
        for x in range(map.width):
            wall = map.tiles[x][y].blocking_sight

            if wall:
                libtcod.console_set_char_background(console, x, y, tile_colors.get('dark_wall'), libtcod.BKGND_SET)
            else:
                libtcod.console_set_char_background(console, x, y, tile_colors.get('dark_ground'), libtcod.BKGND_SET)



# Function that modifies console during runtime.
def consoleRuntime(default_console, root_console):

    for entity in ENTITIES:
        entity.placeEntity()

    # Blitting the console
    libtcod.console_blit(default_console, 0, 0, engine.SCREEN_WIDTH, engine.SCREEN_HEIGHT, root_console, 0, 0)

    # Redraw console
    libtcod.console_flush()
