# Class responsable for storing all active entities.
class EntityStorage:

    # Creates an EntityStorage class, adding the list as an attribute.
    def __init__(self, entityList):
        self.entityList = entityList

    # Returns the current entity list.
    def get_list(self):
        return self.entityList

    # Appends another entity to the list.
    def append_list(self, entity):
        self.entityList.append(entity)
