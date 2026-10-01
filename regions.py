from BaseClasses import Region
from rule_builder.rules import Has

class RegionManager:
    def __init__(self, world, data):
        self.world = world
        self.data = data
        self.connections = []

    def create_and_connect_regions(self):
        self.connect_regions()

    def set_all_rules(self):
        self.set_entrance_rules()
        self.set_completion()

    def add_region(self, name):
        self.world.multiworld.regions.append(Region(name,self.world.player,self.world.multiworld))

    def create_regions(self):
        self.add_region("Menu")
        for character in self.world.character_pool:
            for infamy in range(self.world.options.max_infamy + 1):
                self.add_region(f"{character} Infamy {infamy}")
                if infamy >= 1:
                    self.connections.append((f"{character} Infamy {infamy - 1}", f"{character} Infamy {infamy}"))
            self.connections.append(("Menu", f"{character} Infamy 0"))

    def connect_regions(self):
        for origin, destination in self.connections:
            connect_from = self.world.get_region(origin)
            connect_to = self.world.get_region(destination)
            connect_from.connect(connect_to, f"{origin} -> {destination}")

    def set_entrance_rules(self):
        for entrance in self.world.multiworld.get_entrances(self.world.player):
            if "Menu" in entrance.name:
                character = entrance.name.split()[0]
                self.world.set_rule(entrance, Has(f"{character} Unlock"))

            else:
                infamy = int(entrance.name.split()[-1])
                self.world.set_rule(entrance, Has("Progressive Infamy", infamy))

    def set_completion(self):
        self.world.set_completion_rule(Has("Victory", self.world.options.character_required))