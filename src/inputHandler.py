import tcod as libtcod

# Handles user input.
def handleInput(key,mouse):

    # Checking for a keypress event.
    libtcod.sys_check_for_event(libtcod.EVENT_KEY_PRESS, key, mouse)

    # Getting they key pressed and returning a dictionary:
    # dictionary = {'event_type': event_details}
    if key.vk == libtcod.KEY_UP:
        return {'move': [0, -1]}
    elif key.vk == libtcod.KEY_DOWN:
        return {'move': [0, 1]}
    elif key.vk == libtcod.KEY_LEFT:
        return {'move': [-1, 0]}
    elif key.vk == libtcod.KEY_RIGHT:
        return {'move': [1, 0]}
    else:
        return {}
