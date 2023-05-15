class Garden:
    """
    Garden class for first python lab
    """
    __instance = None

    def __init__(self, area=None, has_orchard=None, has_vegetable_garden=None, number_of_flowers=None):
        self.area = area
        self.has_orchard = has_orchard
        self.has_vegetable_garden = has_vegetable_garden
        self.number_of_flowers = number_of_flowers

    def __str__(self):
        return f"{self.area}, {self.has_orchard}, " \
               f"{self.has_vegetable_garden}, {self.number_of_flowers}"

    def plant_flower(self, number_to_plant):
        self.number_of_flowers = self.number_of_flowers + number_to_plant

    def pluck_flower(self, number_to_remove):
        if self.number_of_flowers <= number_to_remove:
            self.number_of_flowers = 0
        else:
            self.number_of_flowers = self.number_of_flowers - number_to_remove

    def build_orchard(self):
        if not self.has_orchard:
            self.has_orchard = True
        else:
            return

    def destroy_orchard(self):
        if not self.has_orchard:
            return
        else:
            self.has_orchard = False

    def build_vegetable_garden(self):
        if not self.has_vegetable_garden:
            self.has_vegetable_garden = True
        else:
            return

    def destroy_vegetable_garden(self):
        if not self.has_vegetable_garden:
            return
        else:
            self.has_vegetable_garden = False

    @classmethod
    def get_instance(cls):
        if cls.__instance is None:
            cls.__instance = Garden()
        return cls.__instance
