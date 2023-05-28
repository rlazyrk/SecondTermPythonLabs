"""
File for Manager class
"""
# pylint: disable = import-error
from models.garden import Garden
from decorators.log_decorator import loging_decorator
from decorators.iterable_decorator import iterable_decorator


class GardenManager:
    """
    GardenManager class
    """

    def __init__(self, list_of_gardens=None):
        self.list_of_gardens = [] if not list_of_gardens else list_of_gardens

    @loging_decorator
    @iterable_decorator
    def find_all_with_flowers_more_than(self, number_for_comparison: int) -> list:
        """
        :param number_for_comparison:
        :return: list with gardens with more flowers than number_to_compare
        """
        # pylint: disable = line-too-long
        return list(filter(lambda garden: garden.number_of_flowers > number_for_comparison, self.list_of_gardens))

    @loging_decorator
    def add_garden(self, garden_to_add) -> None:
        """
        :param garden_to_add:
        :return: None
        """
        if isinstance(garden_to_add, list):
            self.list_of_gardens.extend(garden_to_add)
        self.list_of_gardens.append(garden_to_add)

    @iterable_decorator
    def find_all_with_orchard(self) -> list:
        """
        :return: list of gardens with orchard
        """
        return list(filter(lambda garden: garden.has_orchard(), self.list_of_gardens))

    @loging_decorator
    def find_all_with_vegetable_garden(self) -> list:
        """
        :return: list of gardens with vegetable garden
        """
        return list(filter(lambda garden: garden.has_vegetable_garden(), self.list_of_gardens))

    @loging_decorator
    def find_all_with_area_smaller_than(self, number_to_compare: int) -> list:
        """
        :param number_to_compare:
        :return: list of gardens with area smaller than number to compare
        """
        return list(filter(lambda garden: garden.area <= number_to_compare, self.list_of_gardens))

    def __len__(self):
        return len(self.list_of_gardens)

    def __iter__(self):
        return iter(self.list_of_gardens)

    def __getitem__(self, item: int) -> Garden:
        if item > self.__len__():
            raise IndexError
        return self.list_of_gardens[item]

    @loging_decorator
    def plant_flower_for_all(self, number_to_add: int) -> list:
        """
        :param number_to_add:
        :return: list with result after add flowers to every garden in manager
        """
        return list([item.number_of_flowers + number_to_add for item in self.list_of_gardens])

    @loging_decorator
    def enumerate_gardens(self):
        """
        :return:
        """
        return enumerate([str(i) for i in self.list_of_gardens])

    @loging_decorator
    def get_all_flowers(self):
        """
        :return:
        """
        return [item.number_of_flowers for item in self.list_of_gardens]

    @loging_decorator
    def check_flower_count(self, request):
        """
        :param request
        :return: dictionary
        """
        temp_list = [item.number_of_flowers > request for item in self.list_of_gardens]
        return {"all": all(temp_list), "any": any(temp_list)}
