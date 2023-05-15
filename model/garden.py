class Garden:
    """
    Garden class for first python lab
    """
    __instance = None

    def __init__(self, area=None, has_orchard=None, has_vegetable_garden=None, number_of_flowers=None):
        self.__area = area
        self.__has_orchard = has_orchard
        self.__has_vegetable_garden = has_vegetable_garden
        self.__number_of_flowers = number_of_flowers

    def __str__(self):
        return f"Area->{self.__area}, Has Orchard->{self.__has_orchard}, "\
               f"Has vegetable garden->{self.__has_vegetable_garden}, Number of flowers->{self.__number_of_flowers}"

    def plant_flower(self, number_to_plant):
        self.__number_of_flowers = self.__number_of_flowers + number_to_plant

    def pluck_flower(self, number_to_remove):
        if self.__number_of_flowers <= number_to_remove:
            self.__number_of_flowers = 0
        else:
            self.__number_of_flowers = self.__number_of_flowers - number_to_remove

    def build_orchard(self):
        if not self.__has_orchard:
            self.__has_orchard = True
        else:
            return

    def destroy_orchard(self):
        if not self.__has_orchard:
            return
        else:
            self.__has_orchard = False

    def build_vegetable_garden(self):
        if not self.__has_vegetable_garden:
            self.__has_vegetable_garden = True
        else:
            return

    def destroy_vegetable_garden(self):
        if not self.__has_vegetable_garden:
            return
        else:
            self.__has_vegetable_garden = False

    @staticmethod
    def get_instance():
        Garden.instance = Garden()
        return Garden.instance

    @property
    def area(self):
        return self.__area

    @area.setter
    def area(self, area_to_set):
        self.__area = area_to_set

    @property
    def number_of_flowers(self):
        return self.__number_of_flowers

    @number_of_flowers.setter
    def number_of_flowers(self, flowers_to_set):
        self.__number_of_flowers = flowers_to_set

    """
    has_orchard setter should be True of False
    """
    @property
    def has_orchard(self):
        return self.__has_orchard

    @has_orchard.setter
    def has_orchard(self, set_orchard):
        self.__has_orchard = set_orchard

    """
    has_vegetable_garden setter should be True of False
    """
    @property
    def has_vegetable_garden(self):
        return self.__has_vegetable_garden

    @has_vegetable_garden.setter
    def has_vegetable_garden(self, set_vegetable_garden):
        self.__has_vegetable_garden = set_vegetable_garden
