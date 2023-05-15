"""
Below is class for first lab
"""


class Garden:
    """
    Garden class for first python lab
    """
    __instance = None

    # pylint: disable = line-too-long
    def __init__(self, area=None, has_orchard=None, has_vegetable_garden=None, number_of_flowers=None):
        self.__area = area
        self.has_orchard = has_orchard
        self.has_vegetable_garden = has_vegetable_garden
        self.number_of_flowers = number_of_flowers

    def __str__(self):
        return f"{self.__area}, {self.has_orchard}, " \
               f"{self.has_vegetable_garden}, {self.number_of_flowers}"

    def plant_flower(self, number_to_plant):
        """
        :param number_to_plant:
        :return: None
        """
        self.number_of_flowers = self.number_of_flowers + number_to_plant

    def pluck_flower(self, number_to_remove):
        """
        :param number_to_remove:
        :return: None
        """
        if self.number_of_flowers <= number_to_remove:
            self.number_of_flowers = 0
        else:
            self.number_of_flowers = self.number_of_flowers - number_to_remove

    def build_orchard(self):
        """
        :return: None
        """
        if not self.has_orchard:
            self.has_orchard = True
        else:
            return

    def destroy_orchard(self):
        """
        :return: None
        """
        if self.has_orchard is True:
            self.has_orchard = False
        else:
            return

    def build_vegetable_garden(self):
        """
        :return: None
        """
        if not self.has_vegetable_garden:
            self.has_vegetable_garden = True
        else:
            return

    def destroy_vegetable_garden(self):
        """
        :return: True or False
        """
        if self.has_vegetable_garden is True:
            self.has_vegetable_garden = False
        else:
            return

    @classmethod
    def get_instance(cls):
        """
        :return: instance of this class
        """
        if cls.__instance is None:
            cls.__instance = Garden()
        return cls.__instance
