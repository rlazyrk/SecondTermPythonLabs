"""
Module for set manager
"""


class GardenSM:
    """
    set manager class
    """

    def __init__(self, regular_manager):
        self.regular_manager = regular_manager
        # pylint: disable = line-too-long
        self.list_of_flower_type = [flower_type for garden in regular_manager.list_of_gardens for flower_type in garden]

    def __iter__(self):
        return iter(self.list_of_flower_type)

    def __next__(self):
        return next(self.__iter__())

    def __len__(self):
        return len(self.list_of_flower_type)

    def __getitem__(self, request):
        if request > self.__len__():
            raise IndexError
        return self.list_of_flower_type[request]
