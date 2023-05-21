"""
file with University garden class
"""
# pylint: disable = import-error
from models.garden import Garden


class UniversityGarden(Garden):
    """
    University garden class
    """

    # pylint: disable = line-too-long
    def __init__(self, area: int = None, number_of_flowers: int = None, number_of_sculpture: int = None):
        Garden.__init__(self, area, number_of_flowers)
        self.number_of_sculpture = number_of_sculpture

    def __str__(self):
        return f"UniversityGarden(area={self.area}, number_of_flowers={self.number_of_flowers}, " \
               f"number_of_sculpture={self.number_of_sculpture})"

    def has_orchard(self) -> bool:
        """
        Always return Flase
        :return:
        """
        return False

    def has_vegetable_garden(self) -> bool:
        """
        Always return False
        :return:
        """
        return False

    def add_sculpture(self, amount_to_add: int) -> None:
        """
        :param amount_to_add:
        :return:
        """
        self.number_of_sculpture = self.number_of_sculpture + amount_to_add

    def remove_sculpture(self, amount_to_remove: int) -> None:
        """
        :param amount_to_remove:
        :return:
        """
        if self.number_of_sculpture <= amount_to_remove:
            self.number_of_sculpture = 0
        self.number_of_sculpture = self.number_of_sculpture - amount_to_remove
