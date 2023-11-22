from Item import Item

class Location:
    def __init__(self, desc, thing=None):
        self.desc = desc
        self.thing = thing
        self.neighbors = {}

    def get_item(self):
        return self.thing

    def get_description(self):
        return self.desc

    def set_item(self, thing):
        self.thing = thing

    def has_item(self):
        if self.thing is None:
            return False
        else:
            return True

    def add_neighbor(self, dir, loc):
        self.neighbors[dir] = loc

    def get_neighbor(self, dir):
        if dir in self.neighbors:
            return self.neighbors[dir]
        else:
            return None

    def remove_item(self):
        temp = self.thing
        self.thing = None
        return temp

    def __str__(self):
        desc_str = ''
        #if self.thing is False:
        desc_str = f'You are {self.desc}'
        #if self.thing is True:
            #item_desc = Item.get_description()
            #desc_str = f'You are {self.desc}\nYou see {item_desc}'
        return desc_str

