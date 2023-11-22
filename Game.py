from Item import Item
from Location import Location


class Game:
    def __init__(self, ll=[], il={}, p=[], cm='', cl=None):
        self.location_list = ll
        self.item_list = il
        self.pouch = p
        self.current_message = cm
        self.current_location = cl

        self.create_world()
        self.current_location = self.Forest
        self.current_message = self.set_welcome_message()

    def get_message(self):
        return self.current_message

    def get_current_location(self):
        return self.current_location

    def create_world(self):
        self.Key = ('Car Keys', 'keys to a car', 5, False)
        self.Medicine = ('Medicine', 'a bottle of medicine on the counter', 5, True)
        self.Crowbar = ('Crowbar', 'a crowbar that adds strength to lift... or to fight', 20, False)
        self.Map = ('Map', 'a map to help you find an item', 10, False)

        self.Forest = Location('in the forest surrounded by trees with a few lights in the distance')
        self.Campground = Location('in a campground, seemingly deserted but the fire is still going')
        self.Lake = Location('at the lake, the boats have all gone missing')
        self.Parking_lot = Location('in the parking lot, there is only one car, but where is the key?')
        self.Cabins = Location('at the cabins, all of the doors appear to have been forced open...')
        self.WatchTower = Location('at the watchtower, you may get a vantage point')
        self.Infirmary = Location('at the infirmary, you may find something to heal yourself')
        self.Cave = Location('at the cave, something has been dragged inside')

        # Forest neighbors
        self.Forest.add_neighbor('North', self.Campground)

        # Campground neighbors
        self.Campground.add_neighbor('North', self.Cabins)
        self.Campground.add_neighbor('West', self.Lake)
        self.Campground.add_neighbor('East', self.Cave)
        self.Campground.add_neighbor('South', self.Forest)

        # Lake neighbors
        self.Lake.add_neighbor('North', self.Parking_lot)
        self.Lake.add_neighbor('East', self.Campground)

        # Parking Lot neighbors
        self.Parking_lot.add_neighbor('East', self.Cabins)
        self.Parking_lot.add_neighbor('South', self.Lake)

        # Cabins neighbors
        self.Cabins.add_neighbor('North', self.WatchTower)
        self.Cabins.add_neighbor('West', self.Lake)
        self.Cabins.add_neighbor('East', self.Infirmary)
        self.Cabins.add_neighbor('South', self.Campground)

        # Watchtower neighbors
        self.WatchTower.add_neighbor('South', self.Cabins)

        # Infirmary neighbors
        self.Infirmary.add_neighbor('West', self.Cabins)
        self.Infirmary.add_neighbor('South', self.Cave)

        # The Cave neighbors
        self.Cave.add_neighbor('North', self.Infirmary)
        self.Cave.add_neighbor('West', self.Campground)

    def go(self, dir):
        next = self.current_location.get_neighbor(dir)
        if next is None:
            self.msg = 'You can\'t move in that direction'
        else:
            self.current_location = next
            self.current_message = self.current_location.__str__()

    def set_welcome_message(self):
        return (f'You wake up in the forest dazed and confused. You are surrounded'
                f' by nothing but endless forest except for a few lights up ahead. '
                f'Upon further inspection you discover you are at a summer camp but '
                f'something is off. The tents have been torn apart and there is '
                f'blood covering the cabin walls, someone must have done this, or '
                f'some thing…. Make your way around the camp to find items to help '
                f'you escape, but be careful, it may be watching…')

    def parse_command(self):
        words = input("Enter>>> ").split()
        first = words[0]
        if len(words) > 1:
            second = words[1]
        else:
            second = None
        return first, second

    def start(self):
        print(self.get_message())

        first, second = self.parse_command()
        if first == "go":
            self.go(second)
        elif first == "look":
            self.look()

    def look(self):
        self.current_message = str(self.current_location)
        return self.current_message

    def help(self):
        hint = 'Update later'
        self.current_message = hint
        return self.current_message

    def pickup(self):
        self.item_list.append(Location.get_item())


