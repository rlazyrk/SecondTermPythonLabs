"""
File for Manager class
"""


class GardenManager:
    """
    GardenManager class
    """

    def __init__(self, list_of_gardens=None):
        if list_of_gardens is None:
            list_of_gardens = []
        self.list_of_gardens = list_of_gardens

    def find_all_with_flowers_more_than(self, number_for_comparison):
        """
        :param number_for_comparison:
        :return:
        """
        # pylint: disable = line-too-long
        return list(filter(lambda garden: garden.number_of_flowers > number_for_comparison, self.list_of_gardens))

    def add_garden(self, garden_to_add):
        """
        :param garden_to_add:
        :return:
        """
        self.list_of_gardens.append(garden_to_add)

    def find_all_with_orchard(self):
        """
        :return: list of gardens with orchard
        """
        return list(filter(lambda garden: garden.has_orchard() is True, self.list_of_gardens))

    def find_all_with_vegetable_garden(self):
        """
        :return: list of gardens with vegetable garden
        """
        # pylint: disable = line-too-long
        return list(filter(lambda garden: garden.has_vegetable_garden() is True, self.list_of_gardens))

    def find_all_with_area_smaller_than(self, number_to_compare):
        """
        :param number_to_compare:
        :return: list of gardens with area smaller than number to compare
        """
        return list(filter(lambda garden: garden.area <= number_to_compare, self.list_of_gardens))
