"""
Class file for Decorative garden class
"""
# pylint: disable = import-error
from models.garden import Garden


class DecorativeGarden(Garden):
    """
    Decorative garden class
    """

    # pylint: disable = line-too-long
    def __init__(self, area: int = None, number_of_flowers: int = None, number_of_flowerbeds: int = None):
        Garden.__init__(self, area, number_of_flowers)
        self.number_of_flowerbeds = number_of_flowerbeds

    def __str__(self):
        return f"DecorativeGarden(area={self.area}, number_of_flowers={self.number_of_flowers}, " \
               f"number_of_flowerbeds={self.number_of_flowerbeds})"

    def has_orchard(self) -> bool:
        """
        Always return false
        :return:
        """
        return False

    def has_vegetable_garden(self) -> bool:
        """
        Always return false
        :return:
        """
        return False

    def add_flowerbed(self, amount_to_add: int) -> None:
        """
        :param amount_to_add:
        :return:
        """
        self.number_of_flowerbeds = self.number_of_flowerbeds + amount_to_add

    def remove_flowerbed(self, amount_to_remove: int) -> None:
        """
        :param amount_to_remove:
        :return:
        """
        if self.number_of_flowerbeds <= amount_to_remove:
            self.number_of_flowerbeds = 0
        self.number_of_flowerbeds = self.number_of_flowerbeds - amount_to_remove
