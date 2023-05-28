"""
class file for farm garden
"""
# pylint: disable = import-error
from models.garden import Garden


class FarmGarden(Garden):
    """
    Farm garden class
    """

    # pylint: disable = line-too-long
    def __init__(self, area: int = None, number_of_flowers: int = None, number_of_tree: int = None,
                 number_of_crops: int = None):
        super().__init__(area, number_of_flowers, ["Tulip", "Rose"])
        self.number_of_tree = number_of_tree
        self.number_of_crops = number_of_crops

    def __str__(self):
        return f"FarmGarden(number_of_crops={self.number_of_crops}, number_of_tree={self.number_of_tree}," \
               f" {super().__str__()} "

    def has_orchard(self):
        """
        Always return True
        :return:
        """
        return True

    def has_vegetable_garden(self):
        """
        Always return True
        :return:
        """
        return True

    def plant_tree(self, amount_to_add: int) -> None:
        """
        :param amount_to_add:
        :return:
        """
        self.number_of_tree = self.number_of_tree + amount_to_add

    def remove_tree(self, amount_to_remove: int) -> None:
        """
        :param amount_to_remove:
        :return:
        """
        if self.number_of_tree <= amount_to_remove:
            self.number_of_tree = 0
        self.number_of_tree = self.number_of_tree - amount_to_remove

    def add_crops(self, amount_to_add: int) -> None:
        """
        :param amount_to_add:
        :return:
        """
        self.number_of_crops = self.number_of_crops + amount_to_add

    def remove_crops(self, amount_to_remove: int) -> None:
        """
        :param amount_to_remove:
        :return:
        """
        if self.number_of_crops <= amount_to_remove:
            self.number_of_crops = 0
        self.number_of_crops = self.number_of_crops - amount_to_remove
