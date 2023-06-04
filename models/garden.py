"""
Below is class for first lab
"""
from abc import ABC, abstractmethod


class Garden(ABC):
    """
    Garden class for first python lab
    """

    def __init__(self, area, number_of_flowers, types_of_flower):
        self.area = area
        self.number_of_flowers = number_of_flowers
        self.type_of_flowers = types_of_flower

    def __str__(self):
        return f"area={self.area}, number_of_flowers={self.number_of_flowers}" \
               f", types_of_flowers={self.type_of_flowers}"

    def plant_flower(self, number_to_plant: int) -> int:
        """
        :param number_to_plant:
        :return: None
        """
        self.number_of_flowers = self.number_of_flowers + number_to_plant
        return self.number_of_flowers

    def pluck_flower(self, number_to_remove: int) -> None:
        """
        :param number_to_remove:
        :return: None
        """
        if self.number_of_flowers <= number_to_remove:
            self.number_of_flowers = 0
        self.number_of_flowers = self.number_of_flowers - number_to_remove

    @abstractmethod
    def has_orchard(self):
        """
        :return:
        """

    @abstractmethod
    def has_vegetable_garden(self):
        """
        :return:
        """

    def dict_by_type(self, type_of_attribute):
        """
        :param type_of_attribute: 
        :return:
        """
        # pylint: disable = line-too-long
        return dict({key: value for key, value in self.__dict__.items() if isinstance(value, type_of_attribute)})

    def __iter__(self):
        return iter(self.type_of_flowers)
