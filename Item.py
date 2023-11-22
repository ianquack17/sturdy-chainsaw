class Item:
    def __init__(self, name, desc, weight, edible):
        self.name = name
        self.desc = desc
        self.weight = weight
        self.edible = edible

    def __str__(self):
        return self.desc

    def is_edible(self):
        return self.edible

    def get_weight(self):
        return self.weight

    def get_name(self):
        return self.name

    def get_description(self):
        return self.desc

    def set_weight(self, wt):
        self.weight = wt

    def set_name(self, name):
        self.name = name

    def set_description(self, desc):
        self.desc = desc

    def set_edible(self, edible):
        self.edible = edible


car_keys = Item('Car Keys', 'keys to a car', 5, False)

