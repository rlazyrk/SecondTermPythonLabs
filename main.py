"""
Main file for tests
"""

from managers.garden_manager import GardenManager
from models.botanic_garden import BotanicGarden
from models.farm_garden import FarmGarden
from models.decorative_garden import DecorativeGarden
from models.university_garden import UniversityGarden

list_of_gardens = [BotanicGarden(10, 23, 13), FarmGarden(25, 102, 44, 342), UniversityGarden(27, 444, 325),
                   DecorativeGarden(20, 45, 55)]

manager = GardenManager(list_of_gardens)
list_with_orchard = manager.find_all_with_orchard()
for i in list_with_orchard:
    print(i)
list_with_area_smaller_than = manager.find_all_with_area_smaller_than(20)
for i in list_with_area_smaller_than:
    print(i)
list_with_flowers_more_than = manager.find_all_with_flowers_more_than(100)
for i in list_with_flowers_more_than:
    print(i)
