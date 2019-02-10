# Class responsable for storing all active entities.
class EntityStorage:


    # Entities are stored as a list (entityList) as an attribute of the object.
    # This may be moved to a different data structure in future (such as a map).
    def __init__(self, entityList):
        self.entityList = entityList

    # Returns the current list of active entities.
    def get_list(self):
        return self.entityList

    # Appends another entity to the list.
    def append_list(self, entity):
        self.entityList.append(entity)
