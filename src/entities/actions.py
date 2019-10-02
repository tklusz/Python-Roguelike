import entities.entity
import mapping.map
import renderer
import entities.fov as fov

# Performs an entity's actions based on the action event.
class Action:

    # Constructor for creating the Action, and getting the event type.
    def __init__(self, action_type, default_map, entity, fov_map):
        """
        Parameters
        ----------
        action_type: string.
            Type of action to perform.
        default_map: map object.
            The map the entity is located on.
        entity: entity object.
            The entity peforming the event.
        fov_map: map object.
            A libtcod map object used for FOV.
        """

        self.action = action_type
        self.default_map = default_map
        self.entity = entity
        self.fov_map = fov_map

        move_event = self.action.get("move")

        # If the event is a movement event, then perform the move action.
        if move_event:
            self._move_action(move_event)

    # This is performed if the action is a movement action.
    def _move_action(self, movement_event):

        # Getting the new absolute x and y positions from the event.
        x_update = movement_event[0]
        y_update = movement_event[1]

        # Getting entity's positions.
        positions = self.entity.get_position()
        positions[0] += x_update
        positions[1] += y_update

        # Only allow the entity to move if the map isn't blocking movement.
        if not self.default_map.is_blocking_movement(positions[0], positions[1]):

            # Updating the new absolute position.
            self.entity.update_position(positions, self.fov_map)

            # Will only occur if the entity is the player.
            if self.entity.is_player:

                # Updating FOV since the player moved.
                fov.compute_fov(self.fov_map, self.entity.x_position, self.entity.y_position)

                # Rendering the FOV portion of the map again.
                # The rest of the map is generated back in the engine.py file.
                renderer.render_fov_map(self.entity.console, self.default_map, self.fov_map)
