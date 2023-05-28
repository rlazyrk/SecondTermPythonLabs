"""
Below is class for first lab
"""
from abc import ABC
from abc import abstractmethod


class Garden(ABC):
    """
    Garden class for first python lab
    """

    def __init__(self, area, number_of_flowers):
        self.area = area
        self.number_of_flowers = number_of_flowers

    def __str__(self):
        return f"{self.area}, {self.number_of_flowers}"

    def plant_flower(self, number_to_plant: int) -> None:
        """
        :param number_to_plant:
        :return: None
        """
        self.number_of_flowers = self.number_of_flowers + number_to_plant

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
