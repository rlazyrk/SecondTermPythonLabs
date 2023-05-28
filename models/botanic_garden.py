"""
Botanic class for lab №2
"""
# pylint: disable = import-error
from models.garden import Garden


class BotanicGarden(Garden):
    """
    Garden class for first python lab
    """

    # pylint: disable = line-too-long
    def __init__(self, area: int = None, number_of_flowers: int = None, number_of_greenhouse: int = None):
        super().__init__(area, number_of_flowers, ["Magnolias", "Witch hazel"])
        self.number_of_greenhouse = number_of_greenhouse

    def __str__(self):
        return f"BotanicGarden(number_of_greenhouse={self.number_of_greenhouse} {super().__str__()})"

    def has_vegetable_garden(self) -> bool:
        """
        Always return True
        :return:
        """
        return True

    def has_orchard(self) -> bool:
        """
        Always return True
        :return:
        """
        return True

    def build_greenhouse(self) -> None:
        """
        add 1 greenhouse
        :return:
        """
        self.number_of_greenhouse = self.number_of_greenhouse + 1

    def destroy_greenhouse(self) -> None:
        """
        destroy 1 greenhouse
        if greenhouse is 0 return
        :return:
        """
        if self.number_of_greenhouse != 0:
            self.number_of_greenhouse = self.number_of_greenhouse - 1
